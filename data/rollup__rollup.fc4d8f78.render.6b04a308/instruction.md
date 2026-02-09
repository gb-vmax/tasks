# Bug Report

### Describe the bug

I'm encountering an issue with assignment expressions where the left-hand side is being rendered incorrectly. When the left side of an assignment should be excluded from the output, it's actually being rendered, and when it should be included, it's being excluded instead.

### Reproduction

```js
// Example 1: Simple assignment where left side should be excluded
let x;
x = getValue(); // Expected: getValue(), Actual: x = getValue()

// Example 2: Assignment where left side should be included  
let y = 10;
y = computeValue(); // Expected: y = computeValue(), Actual: computeValue()
```

The behavior seems to be inverted - the condition for rendering is backwards.

### Expected behavior

When the left-hand side of an assignment expression is marked as not included (e.g., during tree-shaking), only the right-hand side should be rendered. When the left-hand side is included, the full assignment should be rendered.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing incorrect output in bundled code where assignments are either missing their left-hand side or including code that should have been tree-shaken away.

---
Repository: /testbed
