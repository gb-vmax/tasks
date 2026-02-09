# Bug Report

### Describe the bug

After a recent update, the sync store's deserialization process seems to be hanging or taking much longer than expected. When loading data that goes through read hooks, there are noticeable delays that weren't present before.

### Reproduction

```js
const store = new Store();

// Add a read hook
store.addHook({
  read: async (ext, value) => {
    // Simple transformation
    return value;
  }
});

// Try to deserialize some data
const result = await store._deserialize('.json', Buffer.from('{"test": "data"}'));
// This now takes significantly longer than before
```

### Expected behavior

Deserialization should complete quickly without unexpected delays. The process should handle read hooks efficiently without introducing artificial wait times.

### System Info
- Node version: 18.x
- Package: @insomnia/sync

---
Repository: /testbed
