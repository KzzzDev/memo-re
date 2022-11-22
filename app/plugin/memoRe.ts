import { App, Component } from "vue";

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

export default createMemoRe({ views: {} });
