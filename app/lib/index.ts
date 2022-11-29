interface MemoReOptions {
  baseUrl: string;
}

interface MemoRe {
  appName: string;
  appVersion: string;
  access: typeof access;
}

export const useMemoRe = (options?: Partial<MemoReOptions>) => {
  const baseUrl = options?.baseUrl ?? process.env.API_SERVER;

  return {
    appName: process.env.npm_package_name,
    appVersion: process.env.npm_package_version,
    access: access(baseUrl),
  };
};

//#region API
interface AccessOptions {
  method: "GET" | "POST" | "PUT" | "DELETE";
  headers: HeadersInit;
}

type ResponseValidator = (res: Response) => boolean;

const defaultResponseValidator: ResponseValidator = (res) => res.status === 200;

type Middleware = (res: Response) => void;

interface Error {
  errors: [{ message: string }];
}

interface ResponseBase {
  status: number;
  error: Error;
}

export type APIResponse<T> = ResponseBase & T;

export type ErrorResponse = ResponseBase;

const access =
  (baseUrl: string) =>
  <T, U = {}>(
    endpoint: string,
    body?: U,
    options?: Partial<AccessOptions>,
    validator?: ResponseValidator,
    ...middleware: Middleware[]
  ) =>
    fetch(`${baseUrl}/${endpoint}`, {
      body: body && JSON.stringify(body),
      method: options?.method ?? "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer <Token>`, // TODO: Use JWT token
        ...options?.headers,
      },
    })
      .then((res) => {
        middleware.map((ware) => ware(res));
        return res;
      })
      .then<APIResponse<T>>((res) => {
        const valid = validator ?? defaultResponseValidator;
        const output = valid(res) ? Promise.resolve : Promise.reject;
        return output(res.json());
      });
//#endregion
