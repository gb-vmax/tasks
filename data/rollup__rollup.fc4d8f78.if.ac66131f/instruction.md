# Bug Report

### Describe the bug

The CLI is not handling stdin input correctly when `command.stdin` is set to a falsy value or when it's undefined. The plugin system seems to skip adding the stdin plugin in cases where it should be included by default.

### Reproduction

```js
// When command.stdin is not explicitly set or is undefined
const command = {};
addCommandPluginsToInputOptions(inputOptions, command);
// stdin plugin is not added, but it should be included by default

// When command.stdin is explicitly set to undefined
const command2 = { stdin: undefined };
addCommandPluginsToInputOptions(inputOptions, command2);
// stdin plugin is also not added
```

### Expected behavior

The stdin plugin should be added to input options unless `stdin` is explicitly set to `false`. When `stdin` is `undefined` or not provided, it should default to being enabled.

Currently it seems like the stdin plugin is only added when `stdin` is explicitly `true`, which breaks the default behavior where stdin should be available unless explicitly disabled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
