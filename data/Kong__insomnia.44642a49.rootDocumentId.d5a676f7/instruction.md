# Bug Report

### Describe the bug

After a recent update, projects are being created without a `rootDocumentId` being set. This causes issues when trying to navigate to or work with the project's root document. The project structure seems incomplete and operations that depend on the root document fail silently or behave unexpectedly.

### Reproduction

```js
// Create a new project
const project = createProject({
  id: 'test-project',
  name: 'My Project'
});

// The rootDocumentId is empty string instead of being properly set
console.log(project.rootDocumentId); // Expected: 'rootDocumentId', Actual: ''
```

### Expected behavior

When a project is created, it should have a valid `rootDocumentId` that points to the project's root document. Currently it's being set to an empty string which breaks the project hierarchy.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
