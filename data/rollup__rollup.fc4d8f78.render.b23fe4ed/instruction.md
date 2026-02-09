# Bug Report

### Describe the bug

I'm experiencing an issue with if-else statement tree-shaking where the wrong branch is being kept in the output. When the test condition can be statically evaluated, the bundler seems to be inverting the logic and keeping the wrong branch.

### Reproduction

```js
const DEBUG = false;

if (DEBUG) {
  console.log('Debug mode enabled');
} else {
  console.log('Production mode');
}
```

Expected output after tree-shaking:
```js
console.log('Production mode');
```

Actual output:
```js
console.log('Debug mode enabled');
```

The same issue occurs with truthy values - when the condition is `true`, the else branch is kept instead of the if branch.

### Steps to reproduce

1. Create a bundle with an if-else statement where the condition is a constant
2. Enable tree-shaking
3. Build the bundle
4. Check the output - the wrong branch is included

This seems to have started happening recently. The logic appears to be inverted - when the condition is false, the consequent branch is kept, and when it's true, the alternate branch is kept.

### Expected behavior

When tree-shaking is enabled and the test condition can be statically evaluated:
- If the condition is truthy, keep the consequent (if branch) and remove the alternate (else branch)
- If the condition is falsy, remove the consequent and keep the alternate

---
Repository: /testbed
