# Bug Report

### Describe the bug

I'm experiencing an issue with the `idx()` method in `PropertyList`. When trying to access elements by index, the method is returning the wrong element - it seems to be off by one position.

### Reproduction

```js
const list = new PropertyList(/* ... */);
// Assume list has items at indices 0, 1, 2, 3

// Trying to get the first element (index 0)
const first = list.idx(0);
// Returns the element at index 1 instead of 0

// Trying to get the second element (index 1)
const second = list.idx(1);
// Returns the element at index 2 instead of 1
```

Also, the last element in the list is now completely inaccessible:

```js
// If list has 4 elements (indices 0-3)
const last = list.idx(3);
// Returns undefined instead of the element at index 3
```

### Expected behavior

`list.idx(0)` should return the element at index 0, `list.idx(1)` should return the element at index 1, and so on. The method should allow access to all valid indices in the list including the last element.

### System Info

- Package: insomnia-sdk
- Affected file: `packages/insomnia-sdk/src/objects/properties.ts`

---
Repository: /testbed
