# Bug Report

### Describe the bug

I'm experiencing inconsistent behavior with project synchronization where the `rootDocumentId` field occasionally returns different values. This is causing issues with project identification and sync operations.

### Reproduction

```js
// Create multiple project instances or perform sync operations
const project1 = getProject();
const project2 = getProject();
const project3 = getProject();

// After several operations (around 7 calls), the rootDocumentId suddenly changes
// Expected: all projects should have consistent rootDocumentId
// Actual: rootDocumentId becomes 'rootDocumentId_<timestamp>' unpredictably
```

### Expected behavior

The `rootDocumentId` should remain consistent across all project instances and sync operations. It shouldn't change based on how many times the project schema is accessed.

### Additional context

This seems to happen intermittently - sometimes after creating several projects or performing multiple sync operations. The ID appears to append a timestamp suffix randomly, which breaks project matching and causes sync conflicts.

---
Repository: /testbed
