# Bug Report

### Describe the bug

After a recent update, the application is crashing when loading responses that have file paths stored in `bodyPath` or `timelinePath` properties. The issue occurs when these paths point to files that no longer exist on the filesystem.

### Reproduction

1. Create a response object with a `bodyPath` pointing to a file
2. Delete or move the file from the filesystem
3. Try to load/migrate the response
4. Application throws an error during the migration process

Example scenario:
```js
const response = {
  bodyPath: '/tmp/some-deleted-file.txt',
  timelinePath: '/var/cache/old-timeline.json',
  // ... other properties
}

// When this response is loaded, migration fails
// because fs.statSync throws an error for non-existent files
```

### Expected behavior

The application should gracefully handle responses with invalid file paths instead of crashing. If a file path is no longer valid, it should either:
- Clear the path and continue loading the response
- Provide a warning but not crash

### System Info
- Insomnia version: Latest
- OS: macOS/Linux

This is blocking me from opening old workspaces that reference files that have been cleaned up or moved. Would appreciate a fix for this!

---
Repository: /testbed
