# Bug Report

### Describe the bug

I'm experiencing an issue with data deserialization in the sync store. When reading data from storage, the deserialized values are not being properly transformed through the hook chain. It seems like only some hooks are being applied, and the transformed data is being discarded.

### Reproduction

```js
// Setup multiple read hooks
const store = new Store();
store.registerHook({
  read: async (ext, value) => {
    // First transformation
    return transformData(value);
  }
});
store.registerHook({
  read: async (ext, value) => {
    // Second transformation
    return furtherTransform(value);
  }
});

// Try to deserialize data
const result = await store._deserialize('.json', buffer);

// Result doesn't include all transformations
console.log(result); // Missing expected transformations
```

### Expected behavior

All registered read hooks should be applied in sequence, with each hook receiving the output of the previous hook. The final transformed value should be what gets deserialized and returned.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
