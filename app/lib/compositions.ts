import { onMounted, reactive, Ref, shallowRef } from "vue";

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
