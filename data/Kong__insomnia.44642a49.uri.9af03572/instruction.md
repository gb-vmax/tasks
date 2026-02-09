# Bug Report

### Describe the bug

After a recent update, importing resources via URI appears to be incomplete or broken. The import process seems to hang or fail silently without completing the import operation.

### Reproduction

```js
// Attempting to import from a URI
await context.data.import.uri('https://example.com/insomnia-export.json');

// The import doesn't complete - nothing gets imported to the project
```

### Expected behavior

The `import.uri()` function should:
1. Fetch the content from the provided URI
2. Scan the resources in the imported content
3. Import those resources into the active project

Currently, it appears the import process is not finishing properly. The function returns but no resources are actually imported into the workspace.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is blocking our automation workflows that rely on programmatic imports. Any help would be appreciated!

---
Repository: /testbed
