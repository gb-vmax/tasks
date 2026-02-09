# Bug Report

### Describe the bug

I'm experiencing an issue with document ID generation in nested directories. When I have docs organized in subdirectories, the IDs are being generated incorrectly. It seems like the logic for computing the directory name prefix is inverted.

### Reproduction

Let's say I have this structure:
```
docs/
  guides/
    01-getting-started.md
    02-advanced.md
```

When I build the docs, the document IDs are not being prefixed with the directory name as expected. Instead, only the root-level docs (in the `.` directory) seem to get the prefix logic applied, which doesn't make sense.

### Expected behavior

Documents in subdirectories like `guides/` should have their IDs prefixed with the directory name (e.g., `guides/getting-started`). The root directory (`.`) should not add any prefix to the ID.

With `numberPrefixParser` enabled, I'd expect the number prefixes to be stripped from the directory names in the ID, but currently it seems to be doing the opposite - keeping them when it should strip, and stripping when it should keep.

### System Info
- Docusaurus version: latest
- Node version: 18.x

Has anyone else run into this? The directory-based ID prefixing seems completely backwards from what the documentation describes.

---
Repository: /testbed
