# Bug Report

### Describe the bug

After a recent update, the export functionality is completely broken. When trying to export any data, the application crashes immediately with a syntax error. The export modal doesn't even open anymore.

### Reproduction

1. Navigate to any workspace
2. Try to export a collection or request
3. Application throws an error before the export type selection modal appears

The error seems to be related to the export module, but I can't get past the initial export attempt to see what's happening.

### Expected behavior

The export type selection modal should open, allowing users to choose their preferred export format (HAR, Insomnia v4, etc.) and complete the export process.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't export any of our API collections anymore. Any help would be appreciated!

---
Repository: /testbed
