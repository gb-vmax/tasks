# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression settings after updating. It seems like the bodyCompression property is being set incorrectly during migration.

### Reproduction

When I have a response object with `bodyCompression` set to any value other than `__NEEDS_MIGRATION__`, it gets reset to `null` instead of being preserved. This is causing my existing responses to lose their compression settings.

For example:
```js
const response = {
  bodyCompression: 'zip'
  // ... other properties
}

// After migration, bodyCompression becomes null instead of staying as 'zip'
```

Similarly, responses that actually need migration (with `bodyCompression: '__NEEDS_MIGRATION__'`) are not being migrated at all and keep the placeholder value.

### Expected behavior

- Responses with `bodyCompression: '__NEEDS_MIGRATION__'` should be migrated to `'zip'`
- Responses with other compression values should keep their existing values unchanged

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
