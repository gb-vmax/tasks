# Bug Report

### Describe the bug

I'm experiencing an issue with document ID generation in nested directories. It seems like the IDs are being computed incorrectly when documents are placed in subdirectories.

When I have docs organized in folders, the document IDs don't include the directory path prefix as expected. This is causing routing issues and incorrect sidebar references.

### Reproduction

Given this structure:
```
docs/
  guide/
    getting-started.md
  api/
    reference.md
```

The document IDs are being generated without the directory prefix. For example, `guide/getting-started` should have the ID `guide/getting-started`, but it's just coming out as `getting-started`.

This also affects the `numberPrefixParser` option - when I have numbered folders like `01-intro/` and `02-advanced/`, the number prefixes aren't being stripped correctly from the directory names in the ID.

### Expected behavior

- Documents in subdirectories should have IDs that include the directory path (e.g., `guide/getting-started`)
- When `numberPrefixParser` is enabled, number prefixes should be stripped from directory names in the ID
- Documents in the root directory (`.`) should not have any directory prefix in their ID

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
