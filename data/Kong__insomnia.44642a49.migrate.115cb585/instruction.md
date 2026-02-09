# Bug Report

### Describe the bug

After a recent update, API spec documents are being modified unexpectedly during migration. When loading existing specs, their `fileName` and `contentType` properties are being changed even when they shouldn't be, and a new `schemaVersion` property is being added to all documents.

### Reproduction

```js
// Load an existing API spec with the following properties:
const existingSpec = {
  fileName: 'my-api-spec',
  contentType: 'yaml',
  contents: '{"openapi": "3.0.0"}'  // JSON content but contentType says yaml
}

// After migration, the spec is modified:
// - contentType changes from 'yaml' to 'json' 
// - schemaVersion property is added
// - fileName gets trimmed
```

This is causing issues when:
1. Opening previously saved API specs - their properties get changed automatically
2. Specs with intentionally mismatched contentType (for whatever reason) get "corrected"
3. The schemaVersion field appears on all documents even though it wasn't there before

### Expected behavior

Existing API spec documents should not be modified during normal operations. The migration should only run when absolutely necessary, and shouldn't add new properties to documents that don't need them.

### Additional context

This seems to happen every time a spec document is loaded or accessed, not just on actual schema version changes. The migration logic appears to be running unconditionally on all documents.

---
Repository: /testbed
