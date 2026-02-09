# Bug Report

### Describe the bug

When using logical operators (`||` or `&&`) in expressions where one side gets tree-shaken, the generated output includes an extra character from the operator in the final bundle. This causes syntax errors in the generated code.

### Reproduction

```js
// Input code
const result = false || someFunction();

// When the left side (false) is removed during tree-shaking,
// the output incorrectly includes an extra '|' character:
// |someFunction()
// 
// Expected output should be:
// someFunction()
```

This happens when the bundler optimizes logical expressions and removes unreachable branches. The operator position calculation seems to be off by one, leaving part of the operator in the final output.

### Expected behavior

When tree-shaking removes one side of a logical expression, the operator should be completely removed from the output, leaving only the remaining expression without any syntax errors.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
