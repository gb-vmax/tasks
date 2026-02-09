# Bug Report

### Describe the bug

I'm experiencing an issue with data deserialization where the first hook in the hook chain is being skipped. This causes problems when the first registered hook is responsible for critical transformations like decryption or decompression.

### Reproduction

```js
const store = new Store();

// Register multiple hooks
store.addHook({
  read: async (ext, value) => {
    // This first hook is never executed
    return decrypt(value);
  }
});

store.addHook({
  read: async (ext, value) => {
    return decompress(value);
  }
});

// Try to deserialize data
const result = await store._deserialize('.json', encryptedBuffer);
// Result is incorrect because first hook was skipped
```

### Expected behavior

All registered hooks should be executed in order during deserialization, including the first one. The current behavior skips the first hook entirely, which breaks any workflow that relies on the first hook for data transformation.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be a regression from a recent change to the hook processing logic. Any data that requires the first hook to run properly will fail to deserialize correctly.

---
Repository: /testbed
