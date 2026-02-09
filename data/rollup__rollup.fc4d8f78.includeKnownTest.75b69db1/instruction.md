# Bug Report

### Describe the bug

When bundling code with if-else statements where the condition is known at build time, the alternate branch (else block) is being incorrectly included in the output even when the condition is truthy. This results in dead code that should have been tree-shaken appearing in the final bundle.

### Reproduction

```js
// input.js
const DEBUG = true;

if (DEBUG) {
  console.log('Debug mode enabled');
} else {
  console.log('Production mode');
}
```

Expected: Only the consequent branch should be included in the bundle since `DEBUG` is `true`.

Actual: Both branches are included in the output, even though the else block is unreachable.

### Expected behavior

When the test condition of an if-statement can be statically determined to be truthy, the alternate branch should be completely removed from the bundle during tree-shaking. Only the consequent block should remain in the output.

### Additional context

This seems to affect optimization and bundle size, as unreachable code paths are not being properly eliminated when the condition is known to be true at compile time.

---
Repository: /testbed
