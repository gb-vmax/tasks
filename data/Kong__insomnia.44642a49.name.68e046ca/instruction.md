# Bug Report

### Describe the bug

I'm experiencing an issue with the `statusCandidateSchema` where the `name` property is not being returned correctly. It seems like the schema is trying to reference a `name` variable that doesn't exist in the current scope, which causes the property to always return `undefined`.

### Reproduction

```js
const schema = statusCandidateSchema;
const candidate = {
  key: 'test-key',
  name: 'test-name',
  document: someDocument
};

// When using the schema, the name field is not properly extracted
// Expected: 'test-name'
// Actual: undefined
```

### Expected behavior

The `name` property should return the actual name value from the status candidate object, not `undefined`. The schema should properly access and return the name field similar to how the `key` property works.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
