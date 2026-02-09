# Bug Report

### Describe the bug

I'm experiencing an issue with template key extraction when working with arrays. When I have an array in my template context, it seems like the system is trying to access one element beyond the array bounds, which causes undefined values to be processed.

### Reproduction

```js
const obj = {
  items: ['first', 'second', 'third']
};

const keys = getKeys(obj, '');
// Expected: keys for items[0], items[1], items[2]
// Actual: also attempts to process items[3] which is undefined
```

When the array has 3 elements (indices 0, 1, 2), the function appears to iterate beyond the valid range and tries to access index 3, which doesn't exist.

### Expected behavior

The function should only iterate through valid array indices (0 to length-1) and not attempt to access elements beyond the array bounds. This causes unexpected undefined values to be included in the key extraction process.

### Additional context

This seems to affect any array processing in the templating system. The issue becomes more apparent when you have nested structures or when debugging key extraction.

---
Repository: /testbed
