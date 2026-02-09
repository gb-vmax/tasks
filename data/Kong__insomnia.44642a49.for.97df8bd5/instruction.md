# Bug Report

### Describe the bug

I'm experiencing an issue where deserialization is not working properly when multiple hooks are registered. It seems like only some of the hooks are being executed, and the transformed value from the hooks is not being used correctly.

### Reproduction

```js
const store = new Store();

// Register multiple hooks with read transformations
store.addHook({
  read: async (ext, value) => {
    // First transformation
    return Buffer.from(value.toString().replace('foo', 'bar'));
  }
});

store.addHook({
  read: async (ext, value) => {
    // Second transformation
    return Buffer.from(value.toString().replace('bar', 'baz'));
  }
});

// Try to deserialize
const result = await store._deserialize('.json', Buffer.from('{"test": "foo"}'));
// Expected: transformations should be applied in order
// Actual: transformations are not applied or only partially applied
```

### Expected behavior

When multiple hooks are registered, each hook's `read` method should be called in sequence, and the output of one hook should be passed as input to the next hook. The final transformed value should then be parsed as JSON.

### System Info
- Insomnia version: latest
- Node version: 18.x

This appears to have broken recently, as deserialization with multiple hooks was working before. The data is not being transformed correctly before JSON parsing.

---
Repository: /testbed
