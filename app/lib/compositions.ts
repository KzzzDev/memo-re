import { shallowRef } from "vue";

import { APIResponse, BackendCall, ErrorResponse } from ".";

/**
 * @example
 * const { data, error } = useBackend(getUserInfo("IdOfUser"))
 */
export const useBackend = <T>(call: BackendCall<T>, immediately = false) => {
  const data = shallowRef<APIResponse<T>>();
  const error = shallowRef<ErrorResponse>();

  const refresh = () =>
    call()
      .then((res) => (data.value = res))
      .catch((err) => (error.value = err));

  immediately ? refresh() : undefined;

  return { data, error, refresh };
};
