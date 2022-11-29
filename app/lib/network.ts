//#region Prelude
const baseUrl = process.env.API_SERVER;

interface Error {
  errors: [{ message: string }];
}

export interface ResponseBase {
  status: number;
  error: Error;
}

export interface ErrorResponse extends ResponseBase {}

export const access = <T extends ResponseBase, U = {}>(
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
  }).then<T | ErrorResponse>((res) => {
    return (validator(res) ? Promise.resolve : Promise.reject)(res.json());
  });
//#endregion
