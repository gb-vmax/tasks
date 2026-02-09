# Bug Report

### Describe the bug

I'm encountering an issue where assignment expressions with the `=` operator are being incorrectly included in the bundle even when they should be tree-shaken. It seems like the bundler is not properly detecting when simple assignments (as opposed to compound assignments like `+=`, `-=`, etc.) can be safely removed.

### Reproduction

```js
// input.js
let x = 0;

function unused() {
  x = 5; // Simple assignment that should be tree-shaken
}

export function used() {
  return 42;
}
```

When bundling this code, the assignment `x = 5` inside the `unused` function is included in the output even though the function is never called and has no side effects. This bloats the bundle size unnecessarily.

### Expected behavior

Simple assignments using the `=` operator should be tree-shaken when:
1. The assigned variable is not used elsewhere
2. The assignment target has no side effects
3. The function containing the assignment is not included in the bundle

Compound assignments like `+=` or `-=` should continue to be included as they may have side effects.

### Additional context

This appears to be a regression as previous versions correctly tree-shook these assignments. The issue specifically affects the `=` operator while other assignment operators seem to work as expected.

---
Repository: /testbed
