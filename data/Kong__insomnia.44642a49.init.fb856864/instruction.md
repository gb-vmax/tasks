# Bug Report

### Describe the bug

When creating a new API specification, the filename now includes a timestamp that makes it difficult to work with. The filename format has changed from the expected simple format to include date numbers appended to it.

### Reproduction

```js
// Create a new API spec
const newSpec = init();

// Expected filename: "New Document"
// Actual filename: "New Document 20240115" (or similar with current date)
console.log(newSpec.fileName);
```

The filename now has a date stamp automatically appended in the format `YYYYMMDD`, which wasn't the case before.

### Expected behavior

The filename should be simply `New Document` (or whatever the singular document string is) without any automatic timestamp appending. Users should be able to rename it themselves if they want to include dates or other identifiers.

Also, the new spec is being initialized with template content instead of an empty string, which may not be desired in all cases where users want to start from scratch.

### Additional context

This appears to affect all new API spec creation flows. The automatic timestamp makes it harder to predictably reference or test new documents, and the pre-filled template content changes the expected initial state.

---
Repository: /testbed
