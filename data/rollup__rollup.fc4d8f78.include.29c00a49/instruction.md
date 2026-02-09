# Bug Report

### Describe the bug

When using logical OR (`||`) expressions in code that gets tree-shaken, the right-hand side of the expression is not being included in the output bundle even when it should be. This causes runtime errors when the right-hand side contains side effects or is actually needed at runtime.

### Reproduction

```js
// input.js
const config = globalConfig || getDefaultConfig();

function getDefaultConfig() {
  console.log('Getting default config');
  return { theme: 'dark' };
}

export { config };
```

When bundling this code, if `globalConfig` is determined to be falsy, the `getDefaultConfig()` function and its side effects should still be included in the bundle since it will be executed at runtime. However, the function is being incorrectly tree-shaken out.

### Expected behavior

The right-hand side of logical OR expressions should be included in the bundle when it's the branch that will actually be used at runtime, especially when it contains function calls or other expressions with side effects.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
