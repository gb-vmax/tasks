# Bug Report

### Describe the bug

I'm experiencing an issue where return expressions from call expressions are being re-evaluated on every access instead of being cached properly. This is causing significant performance degradation in my build process, especially with complex function call chains.

### Reproduction

```js
// Example code that triggers the issue
function getComplexValue() {
  return expensiveComputation();
}

const result = getComplexValue();
// The return expression gets evaluated multiple times
// instead of using the cached value
```

The problem seems to occur when the same call expression is accessed multiple times during tree-shaking analysis. Instead of returning the cached return expression, it appears to be re-computing it each time.

### Expected behavior

Once a return expression has been determined for a call expression, subsequent accesses should return the cached value without re-evaluating. This was working correctly in previous versions.

### System Info

- Rollup version: Latest main branch
- Node version: 18.x
- OS: Linux

This is causing noticeable slowdowns in larger projects with many function calls. Any help would be appreciated!

---
Repository: /testbed
