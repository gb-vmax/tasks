# Bug Report

### Plugin data storage returning wrapped values instead of actual data

I'm experiencing an issue with the plugin data storage system where retrieved values are coming back in an unexpected format. When I store a simple string value and then retrieve it, I'm getting back a JSON object with metadata instead of the original value.

### Reproduction
```js
// Store a simple value
await upsertByKey('my-plugin', 'user-setting', 'dark-mode');

// Retrieve the value
const doc = await getByKey('my-plugin', 'user-setting');
console.log(doc.value);
// Expected: 'dark-mode'
// Actual: '{"__meta":{"previousValue":null,"lastModified":1234567890,"updateCount":0},"__value":"dark-mode"}'
```

### Expected behavior
The `doc.value` should return the raw string value that was stored ('dark-mode'), not a JSON-serialized wrapper object containing metadata.

### Additional context
This seems to have started recently. The stored values now include internal metadata fields (`__meta`, `__value`) which breaks existing code that expects plain string values. Any plugin or code that reads from the plugin data storage will need to parse this JSON structure to extract the actual value, which is not backward compatible.

---
Repository: /testbed
