import { Component, App } from "vue";

export * from "./helper";
export * from "./compositions";

interface MemoReOptions {
  baseUrl: string;
}

export const useMemoRe = (options?: Partial<MemoReOptions>) => {
  return {
    appName: process.env.npm_package_name,
    appVersion: process.env.npm_package_version,
  };
};

//#region PlugIn
interface MemoReAppOptions {
  views: Record<string, Component>;
}

export const createMemoRe =
  (options: MemoReAppOptions) =>
  (app: App): any => {
    const { views = {} } = options;

    for (const key in views) {
      app.component(key, views[key]);
    }
  };
//#endregion
