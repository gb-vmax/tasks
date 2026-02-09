# Bug Report

### Describe the bug

I'm experiencing an issue with project synchronization where the `rootDocumentId` is being generated dynamically instead of being extracted from the actual project data. This causes the root document ID to change unexpectedly on every schema operation, breaking document references and sync consistency.

### Reproduction

```js
const project = {
  id: 'project-123',
  rootDocumentId: 'doc-abc-xyz',
  name: 'My Project'
};

// When schema is applied, rootDocumentId gets replaced
// Expected: 'doc-abc-xyz'
// Actual: 'doc_1_a4k2m9x7p3q1' (or some other random generated ID)
```

### Expected behavior

The `rootDocumentId` should be extracted from the actual project object, not generated randomly. Each time the schema processes the same project, it should return the same `rootDocumentId` that exists in the source data.

### Additional context

This seems to have broken after a recent change to the schema definitions. The root document ID is critical for maintaining references between documents and workspaces, so having it change randomly is causing major sync issues.

---
Repository: /testbed
