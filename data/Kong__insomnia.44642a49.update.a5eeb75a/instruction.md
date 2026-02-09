# Bug Report

### Describe the bug

I'm experiencing an issue where updating API spec properties doesn't work as expected. When I try to update an API spec with new values, the changes don't seem to persist correctly. It appears that the update operation is not applying the patch data properly.

### Reproduction

```js
const apiSpec = {
  _id: 'spec_123',
  name: 'My API',
  contents: '...'
}

const updates = {
  name: 'Updated API Name',
  contents: 'new contents'
}

// Try to update the spec
await update(apiSpec, updates)

// The name and contents don't get updated as expected
```

### Expected behavior

When calling `update()` with an API spec and a patch object, the patch values should be merged into the spec and the updated spec should be persisted to the database. The new values from the patch should take precedence over the existing values.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
