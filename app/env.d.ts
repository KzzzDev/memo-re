export declare global {
  namespace NodeJS {
    interface ProcessEnv {
      /**
       * Base URL for API endpoints.
       */
      readonly API_SERVER: string;
      /**
       * Key to get/set JWT.
       */
      readonly TOKEN_KEY: string;
      /**
       * Application name injected from package.json
       */
      readonly npm_package_name: string;
      /**
       * Application version injected from package.json
       */
      readonly npm_package_version: string;
    }
  }
}
