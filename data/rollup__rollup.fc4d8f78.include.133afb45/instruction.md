# Bug Report

### Describe the bug

When using `for...of` loops in my code, I'm seeing unexpected behavior where the loop body is being included in the bundle even when the loop variable isn't actually used. This seems to be causing unnecessary code to be included in the output.

### Reproduction

```js
// This for...of loop should be tree-shaken when the loop variable is unused
for (const item of items) {
  // Even when this body doesn't use 'item' or has no side effects,
  // it's still being included in the bundle
}
```

I noticed this after a recent update. Previously, unused for...of loops were being properly tree-shaken, but now they're always included in the output bundle regardless of whether they're actually needed.

### Expected behavior

For...of loops where the loop variable and body are not used should be tree-shaken and excluded from the final bundle, similar to how other unused code is handled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
