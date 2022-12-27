const tokenKey = process.env.VITE_TOKEN_KEY;

export const setToken = (token?: string) => token && localStorage.setItem(tokenKey, token);

export const getAuthHeader = () =>
  ((token: string | null) =>
    token && {
      Authorization: "Bearer " + token,
    })(localStorage.getItem(tokenKey));
