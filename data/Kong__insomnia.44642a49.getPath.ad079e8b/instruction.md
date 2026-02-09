# Bug Report

### Describe the bug
The `app.getPath()` plugin API method is not working correctly after a recent update. When calling `getPath` with valid path names like 'documents' or 'downloads', it throws an error saying the path name is unknown, even though these should be supported paths.

### Reproduction
```js
// In a plugin context
const documentsPath = app.getPath('documents');
// Error: Unknown path name documents

const downloadsPath = app.getPath('downloads');
// Error: Unknown path name downloads
```

The method only seems to work with 'desktop' now, but fails for other common paths that should be supported.

### Expected behavior
The `app.getPath()` method should accept standard path names like 'documents', 'downloads', 'home', 'temp', etc. and return the corresponding system paths without throwing errors.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
