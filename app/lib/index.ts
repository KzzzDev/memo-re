import { access } from "./network";

interface MemoReOptions {
  baseUrl: string;
}

export const useMemoRe = (options?: Partial<MemoReOptions>) => {
  const { baseUrl = process.env.API_SERVER } = (options ??= {});

  return {
    appName: process.env.npm_package_name,
    appVersion: process.env.npm_package_version,
    access,
  };
};
