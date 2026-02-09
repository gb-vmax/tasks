# Bug Report

### Describe the bug

I'm experiencing an issue with the sync schema definitions where the `statusCandidateSchema` appears to have malformed syntax. When trying to use the sync functionality, I'm getting unexpected errors related to schema validation.

### Reproduction

The issue occurs when working with status candidates in the sync module. Here's what I'm seeing:

```js
// Attempting to use statusCandidateSchema
const candidate = {
  key: 'some-key',
  name: 'test-candidate',
  document: someDocument
};

// Schema validation or key generation fails with syntax errors
```

### Expected behavior

The `statusCandidateSchema` should properly define the schema structure with valid syntax, allowing status candidates to be created and validated correctly during sync operations.

### Additional context

This seems to be affecting the sync module's ability to process merge conflicts and status candidates. The schema definition looks like it might have incomplete or incorrectly formatted property definitions.

---
Repository: /testbed
