import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
import env from "vite-plugin-env-compatible";

const { resolve } = require('path')

export default defineConfig({
  plugins: [env({ prefix: "VITE_", mountedPath: "process.env" }), vue()],
  base: "/",
  build: {
    outDir: resolve(__dirname, 'dist'),
    assetsDir: 'static',
    cssCodeSplit: false,
    rollupOptions: {
      external: ["vue"],
      output: {
        format: "iife",
        globals: {
          vue: "Vue",
        },
      },
    },
  },
});
