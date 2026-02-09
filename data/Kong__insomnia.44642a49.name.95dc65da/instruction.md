# Bug Report

### Describe the bug

I'm experiencing an issue where project names are not being properly handled in the sync schema. When working with backend projects, the name field appears to be null instead of containing the actual project name.

### Reproduction

```js
// When syncing a project, the name field is unexpectedly null
const project = {
  id: 'project-123',
  rootDocumentId: 'root-456',
  name: 'My Project'
}

// After schema processing, project.name becomes null instead of 'My Project'
```

### Expected behavior

The project name should be preserved and accessible after schema processing. The name field should return the actual project name string, not null.

### Additional context

This seems to affect project synchronization functionality. Any operations that rely on the project name field may fail or display incorrectly.

---
Repository: /testbed
