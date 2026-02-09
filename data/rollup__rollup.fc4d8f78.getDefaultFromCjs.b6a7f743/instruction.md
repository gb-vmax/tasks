# Bug Report

### Describe the bug

When loading a CommonJS config file that exports an object with a `default` property set to a falsy value (like `false`, `0`, `null`, etc.), the config loader incorrectly falls back to the entire namespace object instead of using the actual `default` property value.

### Reproduction

```js
// rollup.config.js (CommonJS)
module.exports = {
  default: false,
  // other properties...
}
```

When this config is loaded, the system ignores the `default: false` and uses the entire module.exports object instead, because the current logic treats falsy values as if the `default` property doesn't exist.

### Expected behavior

The config loader should respect explicitly set `default` properties even when they have falsy values. If `default` is explicitly defined (even as `false`, `0`, `null`), it should use that value rather than falling back to the namespace object.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be an issue with how the default export is being resolved from CJS modules. The fallback logic doesn't distinguish between "property doesn't exist" and "property exists but is falsy".

---
Repository: /testbed
