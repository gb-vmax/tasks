# Bug Report

### Describe the bug

When using array destructuring with holes (sparse arrays), I'm getting a runtime error. It seems like the code is trying to call methods on `null` elements in array patterns, which crashes the application.

### Reproduction

```js
// This pattern with a hole causes an error
const [a, , c] = [1, 2, 3];

// Also fails with nested destructuring
const [first, , third] = someArray;

// Works fine without holes
const [x, y, z] = [1, 2, 3]; // This works
```

The issue occurs when there's a "hole" in the destructuring pattern (the middle comma with nothing between). The application throws an error trying to process the null element.

### Expected behavior

Array destructuring with holes should work correctly - the skipped positions should simply be ignored and not cause any errors. This is standard JavaScript behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
