# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where it appears to be reading beyond the bounds of an array when processing syntax extensions. This is causing unexpected behavior when multiple syntax extensions are being registered.

### Reproduction

```js
const extensions = [
  { add: 'before', /* ... */ },
  { add: 'after', /* ... */ },
  { add: 'before', /* ... */ }
];

// When processing these extensions, the loop iterates one extra time
// accessing list3[list3.length] which is undefined
```

The issue occurs in the `constructs` function when it's iterating over the list of extensions. The loop condition allows it to go one index past the end of the array.

### Expected behavior

The function should only iterate through valid array indices (0 to length-1) and not attempt to access elements beyond the array bounds. This could lead to undefined values being pushed into the `before` or `existing` arrays.

### Additional context

This seems to affect the syntax extension registration process. When extensions are added, some may not be properly categorized as "before" or "after" due to the off-by-one error in the iteration.

---
Repository: /testbed
