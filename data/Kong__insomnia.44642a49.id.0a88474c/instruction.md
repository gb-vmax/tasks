# Bug Report

### Describe the bug

When working with backend projects, the project ID is coming back as an empty string instead of the expected value. This is causing issues when trying to reference or work with projects since they can't be properly identified.

### Reproduction

```js
const project = {
  id: projectSchema.id(),
  rootDocumentId: projectSchema.rootDocumentId(),
  name: projectSchema.name(),
};

console.log(project.id); // Returns empty string '' instead of 'id'
```

### Expected behavior

The `projectSchema.id()` should return `'id'` as the identifier, not an empty string. Projects need valid IDs to be properly tracked and referenced throughout the application.

### Additional context

This seems to affect project synchronization and backend operations where project identification is critical. Without proper IDs, projects can't be correctly matched or updated.

---
Repository: /testbed
