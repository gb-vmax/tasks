# Bug Report

### Describe the bug

I'm experiencing an issue where return value analysis appears to be duplicating expressions. When analyzing functions with multiple return statements, the return expressions seem to be counted twice, leading to incorrect deoptimization behavior.

### Reproduction

```js
function example(condition) {
  if (condition) {
    return someValue;
  }
  return otherValue;
}
```

When this function is analyzed, each return expression is being registered multiple times internally, which causes the deoptimization logic to behave incorrectly. This affects tree-shaking and dead code elimination.

### Expected behavior

Each return expression should only be registered once in the return value scope. The deoptimization should analyze each unique return path exactly once.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently and is affecting the optimization of my bundle. The bundle size has increased and some code that should be tree-shaken is being retained.

---
Repository: /testbed
