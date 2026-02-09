# Bug Report

### Describe the bug

I'm getting a `ReferenceError` when working with project schemas. The application crashes with `name is not defined` when trying to use the project schema functionality.

### Reproduction

```js
// When attempting to use projectSchema
const schema = projectSchema;
// Triggers: ReferenceError: name is not defined

// The schema tries to reference 'name' but it's not defined in scope
```

### Expected behavior

The `projectSchema` should properly return the string `'name'` for the name field, similar to how `id` returns `'id'` and `rootDocumentId` returns `'rootDocumentId'`.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
