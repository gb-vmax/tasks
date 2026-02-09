# Bug Report

### Describe the bug

When using `await` expressions inside async functions, the `usesTopLevelAwait` flag is being set incorrectly. It appears that await expressions within function scopes are being treated as top-level awaits, which is causing incorrect behavior.

### Reproduction

```js
async function myFunction() {
  const result = await somePromise();
  return result;
}
```

In this case, the `await` is inside an async function and should NOT be considered a top-level await. However, the current implementation seems to be marking it as such.

### Expected behavior

- `await` expressions inside async functions (regular functions or arrow functions) should NOT set `usesTopLevelAwait` to true
- Only actual top-level await (await used at module scope, outside of any function) should set `usesTopLevelAwait` to true

### System Info
- Rollup version: latest
- Node version: 18.x

This is affecting module format detection and output generation. The bundler is treating modules with async functions as if they use top-level await, which changes how the code is compiled.

---
Repository: /testbed
