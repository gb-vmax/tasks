# Bug Report

### Describe the bug

I'm experiencing an issue with function call return type inference in rollup. When a function is called, the return expression seems to be incorrectly resolved, causing the bundler to treat all function calls as returning unknown types regardless of what they actually return.

### Reproduction

```js
function getValue() {
  return 42;
}

const result = getValue();
// rollup treats result as unknown type instead of number
// This affects tree-shaking decisions
```

This seems to affect any code where return type information is important for optimization. The issue appears when the bundler analyzes call expressions - it's not properly tracking what the function returns.

### Expected behavior

The bundler should correctly infer that `getValue()` returns a number and use that information for tree-shaking and optimization decisions. Function call return types should be properly analyzed and cached.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
