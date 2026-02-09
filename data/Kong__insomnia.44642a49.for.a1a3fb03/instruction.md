# Bug Report

### Describe the bug

I'm experiencing an issue with data deserialization after a recent update. When trying to read data from the store, I'm getting a syntax error about an unexpected token. It seems like the deserialization process is failing to properly parse the data.

### Reproduction

```js
const store = new Store();

// Add some hooks for processing data
store.addHook({
  read: async (ext, value) => {
    // Simple transformation hook
    return value;
  }
});

// Try to deserialize some JSON data
const buffer = Buffer.from('{"test": "value"}', 'utf8');
await store._deserialize('json', buffer);
```

### Expected behavior

The data should be deserialized correctly and return a valid JSON object. The hooks should process the data and the final result should be parseable JSON.

### Actual behavior

Getting a parsing error when trying to deserialize. The method seems to be returning something that can't be parsed as JSON. This used to work fine before but now it's consistently failing.

### Additional context

This appears to be affecting all deserialization operations in the store. The issue happens regardless of what hooks are registered or what data is being processed.

---
Repository: /testbed
