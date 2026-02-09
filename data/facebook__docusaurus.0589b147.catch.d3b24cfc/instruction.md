# Bug Report

### Describe the bug

When processing doc metadata fails, the error message shows the wrong information - the file path and version name are swapped in the error output. This makes debugging really confusing because you see the version name where the file path should be and vice versa.

### Reproduction

1. Create a doc file that triggers a metadata processing error (e.g., invalid frontmatter)
2. Observe the error message that gets thrown
3. Notice that the error says something like:
   ```
   Can't process doc metadata for doc at path path=1.0.0 in version name=/docs/my-file.md
   ```
   
The path and version name values are clearly in the wrong positions.

### Expected behavior

The error message should correctly display:
```
Can't process doc metadata for doc at path path=/docs/my-file.md in version name=1.0.0
```

This makes it very difficult to identify which specific file is causing issues when you have metadata processing errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
