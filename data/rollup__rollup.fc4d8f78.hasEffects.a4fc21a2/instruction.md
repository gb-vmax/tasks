# Bug Report

### Describe the bug

Functions marked with `@__PURE__` annotations are not being properly tree-shaken when their arguments have side effects. The pure annotation is being ignored, and the function call is being included in the bundle even though it should be removed.

### Reproduction

```js
function logMessage(msg) {
  console.log(msg);
  return msg;
}

/*@__PURE__*/ someFunction(logMessage('test'));
```

In this case, the `logMessage('test')` call has side effects (console.log), but the pure-annotated function call is still being evaluated and included in the output. The entire expression should be tree-shaken away since the pure function's result is unused.

### Expected behavior

When a function is marked with `@__PURE__`, the tree-shaker should evaluate whether the arguments have side effects BEFORE checking the pure annotation. If the arguments have side effects, those should be preserved, but if the pure function itself is not used, it should still be removed from the bundle.

The current behavior seems to skip checking argument side effects when a pure annotation is present, which leads to incorrect tree-shaking results.

### System Info
- Rollup version: latest
- Node: 18.x

---
Repository: /testbed
