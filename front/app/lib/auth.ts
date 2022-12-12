const { TOKEN_KEY: tokenKey } = process.env;

export const setToken = (token?: string) => token && localStorage.setItem(tokenKey, token);

export const getAuthHeader = () =>
  ((token: string | null) =>
    token && {
      Authorization: "Bearer " + token,
    })(localStorage.getItem(tokenKey));
