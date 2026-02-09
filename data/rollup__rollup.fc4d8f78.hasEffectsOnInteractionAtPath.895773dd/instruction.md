# Bug Report

### Describe the bug

Functions annotated with `@__NO_SIDE_EFFECTS__` are not being properly recognized when called, causing incorrect tree-shaking behavior. The bundler is treating these annotated functions as having side effects even though they're explicitly marked as pure.

### Reproduction

```js
/* @__NO_SIDE_EFFECTS__ */
const pureFunction = () => {
  return { value: 42 };
};

// This should be tree-shaken if the result is unused
const result = pureFunction();
```

When bundling code with arrow functions that have the `@__NO_SIDE_EFFECTS__` annotation, the functions are not being treated as side-effect-free. This means unused calls to these functions are not being eliminated during tree-shaking, leading to unnecessary code in the bundle.

### Expected behavior

Arrow functions with the `@__NO_SIDE_EFFECTS__` annotation should be recognized as pure functions. When their return values are unused, these function calls should be removed during the optimization phase.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
