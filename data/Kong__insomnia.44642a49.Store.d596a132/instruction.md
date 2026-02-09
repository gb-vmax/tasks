# Bug Report

### Describe the bug

I'm experiencing an issue with the sync store where deserialization hooks are not being applied correctly. When reading data from the store, it seems like the hooks are not being awaited properly, causing the deserialization process to fail or return incorrect data.

### Reproduction

```js
// Create a store with a custom read hook
const store = new Store();

store.addHook({
  read: async (ext, value) => {
    // Async transformation
    return await someAsyncTransform(value);
  }
});

// Try to get a value
const result = await store.get('key', 'json');
// Result is a Promise object instead of the actual transformed value
```

### Expected behavior

The store should properly await async read hooks during deserialization and return the fully transformed value. Currently it appears to return Promise objects or fail to apply the transformations at all.

### Additional context

This seems to have started happening recently. The serialization (write) side seems to work fine, but the deserialization (read) side is broken.

---
Repository: /testbed
