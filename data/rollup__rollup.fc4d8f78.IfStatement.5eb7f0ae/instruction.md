# Bug Report

### Describe the bug

I'm experiencing an issue where if-else statements with known test values (like `if (true)` or `if (false)`) are not being optimized correctly during the bundling process. The dead code elimination seems to be inverted - branches that should be removed are being kept, and branches that should be kept might be getting removed.

### Reproduction

```js
// Example 1: This should only include the consequent
if (true) {
  console.log('This should be included');
} else {
  console.log('This should be removed');
}

// Example 2: This should only include the alternate
if (false) {
  console.log('This should be removed');
} else {
  console.log('This should be included');
}

// Example 3: Constant expression that evaluates to truthy/falsy
const DEBUG = false;
if (DEBUG) {
  console.log('Debug code that should be removed');
}
```

### Expected behavior

When the test condition of an if-statement is a known constant value:
- If the test is truthy, only the consequent branch should be included in the output
- If the test is falsy, only the alternate branch (if present) should be included in the output
- Dead branches should be completely eliminated from the bundle

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing my production bundles to include debug code and other conditional branches that should have been eliminated at build time.

---
Repository: /testbed
