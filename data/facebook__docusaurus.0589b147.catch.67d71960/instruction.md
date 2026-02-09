# Bug Report

### Describe the bug

When processing doc metadata fails, the error message shows incorrect information. The error displays `fileName` instead of `filePath` and `versionPath` instead of `versionName`, making it difficult to debug which document is causing the issue.

### Reproduction

1. Create a docs file that will fail metadata processing (e.g., invalid frontmatter)
2. Run the build
3. Check the error message

The error message will show something like:
```
Can't process doc metadata for doc at path path=intro.md in version name=docs
```

But it should show the full file path and correct version name to help locate the problematic file.

### Expected behavior

The error message should include:
- The full file path (`filePath`) to easily locate the file in the project
- The correct version name (`versionName`) 
- The original error cause for better debugging

This makes it much easier to identify and fix issues with doc files, especially in large documentation sites with many files and versions.

---
Repository: /testbed
