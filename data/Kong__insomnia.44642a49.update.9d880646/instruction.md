# Bug Report

### Describe the bug

API spec updates are not working correctly - when trying to update an API spec document, the changes don't get applied properly. It seems like the original document is being ignored and only the patch data is being used.

### Reproduction

```js
const apiSpec = {
  _id: 'spec_123',
  name: 'My API',
  contents: 'openapi: 3.0.0...',
  // ... other properties
}

// Try to update just the name
await update(apiSpec, { name: 'Updated API Name' })

// The update doesn't work as expected - the original apiSpec data is lost
```

### Expected behavior

When calling `update(apiSpec, patch)`, it should merge the patch with the existing apiSpec document. The original document properties should be preserved and only the specified fields in the patch should be updated.

### System Info
- Version: latest
- This appears to affect all API spec update operations

---
Repository: /testbed
