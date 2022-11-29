//#region Prelude
const baseUrl = process.env.API_SERVER;

interface Error {
  errors: [{ message: string }];
}

interface ResponseBase {
  status: number;
  error: Error;
}

export type APIResponse<T> = ResponseBase & T;

export interface ErrorResponse extends ResponseBase {}

export const access = <T, U = {}>(
  endpoint: string,
  body?: U,
  options?: Partial<{
    method: "GET" | "POST" | "PUT" | "DELETE";
    headers: HeadersInit;
  }>,
  validator = (res: Response) => res.status == 200
) =>
  fetch(`${baseUrl}/${endpoint}`, {
    body: body && JSON.stringify(body),
    method: options?.method ?? "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer <Token>`, //! Utilize JWT token
      ...options?.headers,
    },
  }).then<APIResponse<T> | ErrorResponse>((res) => {
    return (validator(res) ? Promise.resolve : Promise.reject)(res.json());
  });
//#endregion
