const tokenKey = process.env.VITE_TOKEN_KEY ?? "jwt";

export const setToken = (token?: string) => token && localStorage.setItem(tokenKey, token);

export const getAuthHeader = () =>
  ((token: string | null) =>
    token && {
      Authorization: "Bearer " + token,
    })(localStorage.getItem(tokenKey));

export const getToken = ()=>{
    return localStorage.getItem(tokenKey)
}


