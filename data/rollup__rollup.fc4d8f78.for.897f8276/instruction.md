# Bug Report

### Describe the bug

I'm experiencing an issue with object destructuring assignment where some properties are not being properly deoptimized. When destructuring objects with multiple properties, it seems like only certain properties trigger the expected behavior while others are skipped entirely.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3, d: 4 };
const { a, b, c, d } = obj;

// Properties at certain positions don't behave correctly
// Expected all properties to be handled the same way
```

This happens with any object pattern that has more than one property. The first property seems to be ignored, then the second one works, third is ignored again, and so on in an alternating pattern.

### Expected behavior

All properties in an object destructuring pattern should be deoptimized consistently, regardless of their position in the pattern. Every property should be treated the same way during assignment deoptimization.

### Additional context

This appears to affect object destructuring in various contexts - function parameters, variable declarations, etc. The behavior is consistent across different object patterns but the alternating skip pattern makes it particularly confusing to debug.

---
Repository: /testbed
