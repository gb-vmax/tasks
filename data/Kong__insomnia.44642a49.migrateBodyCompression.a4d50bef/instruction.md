# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression migration. When responses have a `bodyCompression` value that needs migration, they're not being properly migrated and the compression type is being set incorrectly.

### Reproduction

```js
const response = {
  bodyCompression: '__NEEDS_MIGRATION__',
  // ... other response properties
}

// After migration, bodyCompression should be set to the correct compression type
// but it's not being migrated at all
```

### Expected behavior

Responses with `bodyCompression: '__NEEDS_MIGRATION__'` should be automatically migrated to use the proper compression type. The migration should detect the sentinel value and update it accordingly.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
