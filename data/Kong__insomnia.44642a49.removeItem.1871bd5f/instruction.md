# Bug Report

### Describe the bug

The `store.removeItem()` function in the plugin context doesn't wait for the removal operation to complete before returning. This causes issues when you need to ensure an item is deleted before performing subsequent operations.

### Reproduction

```js
// In a plugin
await store.removeItem('myKey');
// Immediately try to verify deletion
const value = await store.getItem('myKey');
console.log(value); // Still returns the old value instead of null
```

The issue occurs because `removeItem` returns immediately without waiting for the database operation to finish, so any code that runs right after may still see the old data.

### Expected behavior

When calling `await store.removeItem(key)`, the function should wait for the removal to complete before continuing execution. This way, subsequent calls to `getItem` should return `null` for the removed key.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
