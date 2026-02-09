# Bug Report

### Describe the bug
When syncing projects, the project name field is being capitalized incorrectly. The schema is returning 'Name' instead of 'name', which causes issues with the backend API that expects lowercase field names.

### Reproduction
```js
// When creating or syncing a project
const project = {
  id: 'project-123',
  rootDocumentId: 'doc-456',
  name: 'My Project'
}

// The schema transforms this to use 'Name' instead of 'name'
// This breaks API calls that expect lowercase 'name'
```

### Expected behavior
The project schema should use lowercase 'name' to match the backend API expectations and maintain consistency with other fields like 'id' and 'rootDocumentId'.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
