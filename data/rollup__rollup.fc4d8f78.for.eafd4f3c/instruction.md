# Bug Report

### Describe the bug

I'm experiencing an issue with object destructuring where the first property in a destructuring pattern doesn't seem to be handled correctly. When destructuring objects with multiple properties, only properties after the first one are being processed.

### Reproduction

```js
const { a, b, c } = someObject;
// 'a' is not being tracked/optimized properly
// only 'b' and 'c' seem to work as expected
```

This appears to affect any object destructuring pattern where multiple properties are extracted. The first property in the pattern is being skipped entirely.

### Expected behavior

All properties in an object destructuring pattern should be processed equally, including the first one. Each property should be properly deoptimized/tracked regardless of its position in the pattern.

### Additional context

This seems to have started recently. I noticed that when I have destructuring assignments like:

```js
function example({ prop1, prop2, prop3 }) {
  // prop1 behaves differently than prop2 and prop3
}
```

The first property doesn't behave the same way as the others. Not sure if this is related to recent changes in how destructuring is handled internally.

---
Repository: /testbed
