# Bug Report

### Describe the bug

I'm experiencing an issue with the VCS utility functions where keys starting with double underscores (`__`) are being included in the combined map keys output, but they should be filtered out. Additionally, the keys aren't being sorted alphabetically as expected.

### Reproduction

```js
const map1 = {
  'document1': { /* ... */ },
  '__internal': { /* ... */ },
  'document2': { /* ... */ }
};

const map2 = {
  'document3': { /* ... */ },
  '__metadata': { /* ... */ }
};

const keys = combinedMapKeys(map1, map2);
// Current output includes '__internal' and '__metadata'
// Keys are also not sorted alphabetically
```

### Expected behavior

Keys prefixed with `__` should be excluded from the result, and the returned keys should be sorted alphabetically. So for the example above, the expected output would be:
```js
['document1', 'document2', 'document3']
```

### Additional context

This is affecting our sync functionality where internal/private keys are being processed when they shouldn't be. The lack of alphabetical sorting also makes it difficult to maintain consistent ordering across different sync operations.

---
Repository: /testbed
