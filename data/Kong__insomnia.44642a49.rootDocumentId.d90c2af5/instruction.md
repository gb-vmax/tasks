# Bug Report

### Describe the bug
When syncing projects, the `rootDocumentId` is coming back as `undefined` instead of the expected document ID. This breaks project navigation and causes the app to not load the correct root document when opening a synced project.

### Reproduction
```js
// After syncing a project from the backend
const project = await syncProject();

console.log(project.rootDocumentId); 
// Expected: 'rootDocumentId' (string)
// Actual: undefined
```

### Steps to reproduce:
1. Create a new project with documents
2. Sync the project to backend
3. Fetch the project data
4. Check the `rootDocumentId` field - it's undefined

### Expected behavior
The `rootDocumentId` should contain the ID of the root document, not `undefined`. This is needed to properly navigate to the project's main document.

### Additional context
This seems to have broken recently. The project schema should be returning the actual root document ID but it's returning undefined instead.

---
Repository: /testbed
