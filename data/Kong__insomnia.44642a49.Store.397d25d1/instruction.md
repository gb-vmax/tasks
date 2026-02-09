# Bug Report

### Describe the bug

I'm encountering an issue with the sync store where serialization fails when trying to store `Buffer` objects directly. The store seems to be attempting to JSON.stringify Buffer instances, which doesn't work as expected.

### Reproduction

```js
const store = new Store();

// Try to set a Buffer value directly
const bufferData = Buffer.from('test data', 'utf8');
await store.set('test-key', '.bin', bufferData);

// The serialization fails because it tries to JSON.stringify the Buffer
```

### Expected behavior

The store should handle Buffer objects correctly during serialization, preserving the raw binary data without attempting to convert it to JSON. Buffer instances should be passed through directly to the serialization hooks.

### Additional context

This appears to affect any workflow that tries to store binary data directly. The serialization process should distinguish between Buffer objects (which are already in the correct format) and other values that need to be converted to JSON first.

---
Repository: /testbed
