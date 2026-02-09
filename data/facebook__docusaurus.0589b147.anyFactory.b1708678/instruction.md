# Bug Report

### Describe the bug

I'm encountering an issue where the `anyFactory` function appears to be accessing array indices out of bounds. When processing tests, it seems like the loop is iterating one extra time beyond the array length, which could lead to undefined behavior.

### Reproduction

```js
const tests = ['test1', 'test2', 'test3'];
const result = anyFactory(tests);

// The loop condition `++index2 <= tests.length` means it will iterate 
// when index2 equals tests.length, trying to access tests[3] which is undefined
```

### Expected behavior

The function should only iterate through valid array indices (0 to length-1). When the array has 3 elements, it should process indices 0, 1, and 2, not try to access index 3.

### Additional context

This looks like it might cause the `checks` array to have an extra `undefined` element at the end, and the subsequent `any` function might also be affected since it starts from index 0 instead of -1.

---
Repository: /testbed
