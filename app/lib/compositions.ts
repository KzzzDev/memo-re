import { onMounted, reactive, Ref, shallowRef } from "vue";

import { APIResponse, ErrorResponse } from "./network";

type NestedRefs<T> = {
  [key in keyof T]: T[key] extends object ? NestedRefs<T[key]> : Ref<T[key]>;
};

type BackendCall = (...params: any[]) => Promise<APIResponse<any>>;
type BackendCallParameters<T extends BackendCall> = T extends (...args: infer P) => any ? NestedRefs<P> : never;
type BackendCallResponse<T extends BackendCall> = ReturnType<T> extends Promise<infer I> ? I : APIResponse;

/**
 * @example
 * const { data, error } = useBackend(getUserInfo("IdOfUser"))
 */
export const useBackend = <T extends BackendCall>(call: T, immediately = true, ...params: BackendCallParameters<T>) => {
  const data = shallowRef<BackendCallResponse<T>>();
  const error = shallowRef<ErrorResponse>();
  const param = reactive(params);

  const refresh = () =>
    call(...param)
      .then((res) => (data.value = res))
      .catch((err) => (error.value = err));

  if (immediately) {
    onMounted(refresh);
  }

  return { data, error, refresh };
};
