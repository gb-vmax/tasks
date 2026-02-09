# Bug Report

### Describe the bug
I'm experiencing an issue with the deserialization process in the sync store. It appears that the first hook in the hooks array is being skipped during deserialization, which causes data to not be properly processed before being parsed as JSON.

### Reproduction
```js
// Set up multiple hooks for deserialization
store.addHook({
  read: (ext, value) => {
    // This hook should decrypt the data
    return decrypt(value);
  }
});

store.addHook({
  read: (ext, value) => {
    // This hook should decompress the data
    return decompress(value);
  }
});

// Try to deserialize data
const result = await store._deserialize('.json', encryptedData);
// Error: Data is not properly decrypted because the first hook was skipped
```

### Expected behavior
All registered hooks should be executed in order during deserialization. The first hook in the array should not be skipped.

### Additional context
This is causing issues when the first hook is critical for data processing (like decryption or decompression). The data fails to deserialize correctly because it's missing the transformation from the first hook.

---
Repository: /testbed
