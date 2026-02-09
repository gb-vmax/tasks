# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with API spec documents that have missing or invalid `contentType` and `fileName` properties. The application seems to be handling these cases inconsistently, and I'm getting unexpected values when working with older or improperly initialized specs.

### Reproduction

When working with API spec documents that don't have proper initialization:

```js
const apiSpec = {
  _id: 'spec_123',
  parentId: 'wrk_456',
  // contentType is missing or invalid
  contentType: null,
  // fileName is empty or whitespace
  fileName: '   ',
  contents: null
}

// After loading this spec, the contentType and fileName 
// don't get normalized to expected defaults
```

### Expected behavior

- When `contentType` is missing or has an invalid value (not 'json' or 'yaml'), it should default to 'yaml'
- When `fileName` is missing, empty, or just whitespace, it should default to something like "New Document"
- When `contents` is not a string, it should default to an empty string

Currently these fields remain in their invalid state, which causes issues downstream when trying to work with the spec.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be related to how older spec documents are being handled. Would appreciate if the migration logic could properly normalize these fields!

---
Repository: /testbed
