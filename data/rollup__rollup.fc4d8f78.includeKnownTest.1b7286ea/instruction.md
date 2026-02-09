# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where if statements with known constant conditions are including the wrong branch in the output. When the test condition is a truthy constant, the else/alternate branch is being included instead of the then/consequent branch, and vice versa.

### Reproduction

```js
// Input code
if (true) {
  console.log('This should be included');
} else {
  console.log('This should be removed');
}

if (false) {
  console.log('This should be removed');
} else {
  console.log('This should be included');
}
```

After bundling, the output includes the wrong branches - the code that should be tree-shaken away is kept, while the code that should remain is removed.

### Expected behavior

When an if statement has a constant truthy test condition, only the consequent (then) branch should be included in the output. When the test is falsy, only the alternate (else) branch should be included.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
