# Bug Report

### Describe the bug

I'm experiencing an issue with project name handling in the sync schemas. When creating or syncing projects, the name field is being set to an empty string instead of the actual project name. This causes projects to appear without names in the UI.

### Reproduction

```js
// When syncing a project with a name
const project = {
  id: 'test-id',
  rootDocumentId: 'root-doc',
  name: 'My Project'
}

// The projectSchema transforms it incorrectly
// Expected: name should be 'My Project'
// Actual: name becomes ''
```

### Steps to reproduce
1. Create a new project with a name
2. Sync the project using the backend sync functionality
3. Check the project name in the UI - it appears empty

### Expected behavior

The project name should be preserved during sync operations and displayed correctly in the UI. Projects should maintain their assigned names rather than being converted to empty strings.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
