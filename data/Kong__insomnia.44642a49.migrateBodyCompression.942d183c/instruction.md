# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression handling. It appears that the `bodyCompression` field is being set to `'zip'` even when it shouldn't be. This is causing responses that don't need compression migration to have their compression type incorrectly overwritten.

### Reproduction

```js
const response = {
  bodyCompression: null,
  // ... other response fields
};

// After migration runs, bodyCompression becomes 'zip' instead of staying null
migrateBodyCompression(response);
console.log(response.bodyCompression); // Expected: null, Actual: 'zip'
```

The same issue occurs with responses that already have a valid compression type:

```js
const response = {
  bodyCompression: 'gzip',
  // ... other response fields
};

migrateBodyCompression(response);
console.log(response.bodyCompression); // Expected: 'gzip', Actual: 'zip'
```

### Expected behavior

The migration function should only update `bodyCompression` to `'zip'` when the value is specifically `'__NEEDS_MIGRATION__'`. Responses with `null`, `undefined`, or other valid compression types should remain unchanged.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
