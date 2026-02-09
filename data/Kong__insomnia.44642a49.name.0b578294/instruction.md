# Bug Report

### Describe the bug

When syncing projects, the project name is getting truncated by one character. For example, a project named "MyProject" appears as "MyProjec" after sync operations.

### Reproduction

```js
const project = {
  id: '123',
  rootDocumentId: 'root-456',
  name: 'MyProject'
};

// After applying projectSchema
// Expected: name = 'MyProject'
// Actual: name = 'nam' (last character removed)
```

### Steps to reproduce
1. Create a new project with any name
2. Perform a sync operation
3. Check the project name - it will be missing the last character

### Expected behavior
The project name should remain unchanged during sync operations. All characters should be preserved.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
