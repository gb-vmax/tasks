# Bug Report

### Describe the bug

Error messages when processing doc metadata are missing important file path information. When there's an error processing a document, the error message no longer shows which specific file caused the problem, making it very difficult to debug issues.

### Reproduction

1. Create a doc file with invalid metadata or content that causes processing to fail
2. Run the build
3. Observe the error message - it will say something like:
   ```
   Can't process doc metadata for doc at path in version name=current
   ```
   
Notice that the actual file path is missing from the error message. Previously, this would have shown the full path to the problematic file.

### Expected behavior

The error message should include the file path of the document that failed to process, like:
```
Can't process doc metadata for doc at path path=/docs/my-doc.md in version name=current
```

This information is critical for quickly identifying which file needs to be fixed, especially in large documentation sites with many files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
