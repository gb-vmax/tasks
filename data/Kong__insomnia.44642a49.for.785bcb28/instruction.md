# Bug Report

### Describe the bug

After a recent update, the deserialization process in the sync store is completely broken. When trying to deserialize data, I'm getting syntax errors about unexpected tokens in the code.

### Reproduction

```js
const store = new Store();
// Try to deserialize any data with hooks
await store._deserialize('json', Buffer.from('{"test": "data"}'));
```

The above code throws a syntax error immediately when the method is called.

### Expected behavior

The `_deserialize` method should properly iterate through hooks and deserialize the data without any syntax errors. It was working fine before the latest changes.

### Additional context

This seems to have started happening after some modifications to the hook processing logic in the store. The method is not even executing properly - it fails during parsing/compilation rather than at runtime.

---
Repository: /testbed
