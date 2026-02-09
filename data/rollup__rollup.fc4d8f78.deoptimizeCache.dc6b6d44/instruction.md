# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where deoptimization seems to trigger infinite recursion or repeated deoptimization cycles. The bundler appears to get stuck in a loop when processing certain logical expressions (&&, ||, ??) during tree-shaking.

### Reproduction

```js
// Input code that triggers the issue
const result = condition1 && condition2 && condition3;

// Or with nullish coalescing
const value = foo ?? bar ?? baz;
```

When bundling code with nested logical expressions, the process either hangs or takes an extremely long time to complete. This seems to happen specifically when the logical expressions need to be deoptimized during the tree-shaking phase.

### Expected behavior

The bundler should complete the tree-shaking pass without getting stuck in repeated deoptimization cycles. Logical expressions should be deoptimized once and the process should continue normally.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how the deoptimization cache is being managed for logical expressions. The bundler used to handle these cases fine in previous versions.

---
Repository: /testbed
