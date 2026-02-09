# Bug Report

### Describe the bug

I'm experiencing an issue with object merging/extension functionality. When trying to merge plain objects, the behavior seems incorrect - it's treating arrays as plain objects and vice versa.

### Reproduction

```js
const target = { a: 1 };
const source = { b: 2 };

// Merging two plain objects
const result = extend(target, source);
// Expected: { a: 1, b: 2 }
// Actual: Unexpected behavior

// Also, arrays are being treated as plain objects
const arr = [1, 2, 3];
// isPlainObject(arr) returns true when it should return false
```

### Expected behavior

- Plain objects should be correctly identified and merged
- Arrays should NOT be treated as plain objects
- The extend/merge operation should properly combine object properties

### Additional context

This appears to affect the object detection logic. The function that checks whether something is a plain object seems to have the wrong condition - it's checking for arrays instead of objects.

---
Repository: /testbed
