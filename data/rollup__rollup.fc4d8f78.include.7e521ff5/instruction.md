# Bug Report

### Describe the bug

When using binary expressions that can be statically evaluated (like `1 + 1` or `true && false`), the entire expression is being incorrectly excluded from the output bundle. This causes issues when these expressions are part of the code that should be included.

### Reproduction

```js
// Input code
const result = 1 + 1;
console.log(result);

// Expected output: both the assignment and console.log should be included
// Actual output: the expression gets excluded from the bundle
```

Another example:
```js
if (true && someCondition) {
  doSomething();
}

// The binary expression `true && someCondition` is being removed
// even though it's needed for the control flow
```

### Expected behavior

Binary expressions should be included in the output even when they can be statically evaluated to a literal value. The tree-shaking logic should not exclude these expressions when they're part of necessary code paths.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The logic appears to be inverted - expressions are being excluded when they should be included.

---
Repository: /testbed
