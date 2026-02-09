# Bug Report

### Describe the bug

After a recent update, responses with legacy body compression settings are no longer being handled correctly. When loading older response data that has `bodyCompression` set to `__NEEDS_MIGRATION__`, the application fails to properly migrate this value, causing issues with response display and decompression.

### Reproduction

1. Load a response object from storage with the following structure:
```js
{
  _id: 'res_123',
  bodyCompression: '__NEEDS_MIGRATION__',
  // ... other response properties
}
```

2. Try to access or display the response body
3. The body compression handling fails because the migration logic is missing

### Expected behavior

Responses with `bodyCompression: '__NEEDS_MIGRATION__'` should be automatically migrated to use `'zip'` compression format, ensuring backward compatibility with older stored responses.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

This seems like a regression - older responses that were stored before a compression format change are no longer being properly handled.

---
Repository: /testbed
