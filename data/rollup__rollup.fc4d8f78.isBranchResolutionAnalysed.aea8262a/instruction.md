# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in my code where the branch resolution seems to be running infinitely or repeatedly when it shouldn't. The bundler appears to be stuck analyzing logical expressions (`&&`, `||`, `??`) over and over again, leading to performance degradation or hanging.

### Reproduction

```js
// This code causes the bundler to hang or take extremely long to process
const result = condition1 && condition2 && condition3;

// Or with nullish coalescing
const value = a ?? b ?? c;
```

When bundling code that contains logical expressions, especially nested ones, the process either:
1. Takes an extremely long time to complete
2. Gets stuck in what appears to be an infinite loop
3. Eventually times out or crashes

### Expected behavior

Logical expressions should be analyzed once during the bundling process. The branch resolution analysis should complete efficiently without redundant re-analysis.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. Simple logical expressions work fine, but more complex nested ones cause the issue.

---
Repository: /testbed
