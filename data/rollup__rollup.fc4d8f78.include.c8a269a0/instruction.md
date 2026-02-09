# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-in loops where the loop variable is not being properly included in the bundle when `includeChildrenRecursively` is `false`. This causes the generated code to be incomplete or incorrect.

### Reproduction

```js
// input.js
const obj = { a: 1, b: 2, c: 3 };

for (const key in obj) {
  console.log(key);
}
```

When bundling this code, the loop variable `key` is not always included correctly in the output, leading to broken code generation in certain tree-shaking scenarios.

### Expected behavior

The for-in loop variable should always be included in the bundle regardless of the `includeChildrenRecursively` flag value. The generated output should contain valid JavaScript code with all necessary variable declarations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
