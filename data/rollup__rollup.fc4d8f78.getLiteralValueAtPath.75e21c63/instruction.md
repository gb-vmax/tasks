# Bug Report

### Describe the bug

I'm experiencing an infinite loop/stack overflow when trying to get literal values from call expressions in certain scenarios. The bundler hangs and eventually crashes with a maximum call stack size exceeded error.

### Reproduction

This happens when working with code that has function calls where we try to resolve the literal value of the return expression. The issue appears to be related to how return expressions are tracked during recursion.

```js
// Example code that triggers the issue
function getValue() {
  return someFunction();
}

const result = getValue().property;
```

When the bundler tries to analyze this code and resolve literal values, it gets stuck in an infinite recursion loop.

### Expected behavior

The bundler should properly track recursive calls and either resolve the literal value or return `UnknownValue` without hanging or crashing.

### System Info
- Rollup version: latest
- Node version: 18.x

This is blocking our build process. Any help would be appreciated!

---
Repository: /testbed
