import { onMounted, reactive, ref, Ref, shallowRef, UnwrapRef, watch, WatchStopHandle } from "vue";

import { APIResponse, ErrorResponse } from "./network";

type NestedRefs<T> = {
  [key in keyof T]: T[key] extends object ? NestedRefs<T[key]> : Ref<T[key]>;
};

type BackendCall = (...params: any[]) => Promise<APIResponse<any>>;
type BackendCallParameters<T extends BackendCall> = T extends (...args: infer P) => any ? NestedRefs<P> : never;
/**
 * Return type of backend call, basically same as `APIResponse<T>`.
 */
type BackendCallResponse<T extends BackendCall> = ReturnType<T> extends Promise<infer I> ? I : APIResponse;

/**
 * @param call network function.
 * @param immediately whether to invoke the network function immediately on mounted.
 * @param args parameters to call the function.
 * @returns
 * @example
 * const foo = ref("foo")
 * const bar = ref("bar")
 *
 * const { data, error, refresh } = UseBackend(backendCall, true, foo, bar); // will call backendCall(foo, bar)
 * // data will be filled if backend server responded normally.
 * // error will be filled if backend server responded error.
 * // refresh is a function to be call to fetch backend server again.
 */
export const useBackend = <T extends BackendCall>(call: T, immediately = true, ...args: BackendCallParameters<T>) => {
  const data = shallowRef<BackendCallResponse<T>>();
  const error = shallowRef<ErrorResponse>();
  const params = reactive(args);

  const refresh = () =>
    call(...params)
      .then((res) => {
        data.value = res;
        error.value = undefined;
      })
      .catch((err) => {
        error.value = err;
        data.value = undefined;
      });

  if (immediately) {
    onMounted(refresh);
  }

  return { data, error, refresh };
};

/**
 * @param initial Initial value of the composition.
 * @param rules Validation rule, return whether the value is invalid or error message.
 * @param options.immediately Whether to watch the value change immediately.
 * @param options.defaultMessage Default error message. Use when value is invalid and no error message returned.
 */
export const useError = <T>(
  initial: T,
  rules: ((value: UnwrapRef<T>) => boolean | string)[],
  options = { immediately: true, defaultMessage: "" }
) => {
  const data = ref(initial);
  const error = ref<string | undefined>(undefined);

  const predicate = rules.reduce((prev, next) => (value) => next(value) || prev(value));
  const validate = (value: UnwrapRef<T>) => {
    const rst = predicate(value);
    const msg = rst ? (typeof rst == "string" ? rst : options?.defaultMessage) : "";
    error.value = msg || undefined;
    return msg;
  };

  let stop: WatchStopHandle | undefined;
  const start = () => (stop && stop()) || (stop = watch(data, validate, { immediate: true }));

  if (options?.immediately) {
    onMounted(start);
  }

  return { data, error, start, stop, validate };
};
