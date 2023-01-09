# memo:Re App

## Installation

```sh
git clone https://github.com/Kazumasa1/memo-re.git
cd memo-re/app
npm ci
```

## Usage

Run the following command to build this Vue app.
This will build resources that can serve statically to `dist` directory.

```sh
npm run build
```

## Behavior

This app require some environment variables to support.
You can either set those values to environment or in `.env` file.
Refer to [`env.d.ts`](./env.d.ts) for detail.

## Contribute

- Install the workspace recommendation extensions.
- Use the following setting for development vscode workspace.

```json
{
  "volar.completion.preferredTagNameCase": "kebab",
  "volar.completion.preferredAttrNameCase": "kebab"
}
```
