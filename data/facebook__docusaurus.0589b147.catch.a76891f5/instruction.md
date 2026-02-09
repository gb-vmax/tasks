# Bug Report

### Describe the bug

When processing doc metadata fails, the error message doesn't include the file path anymore, making it really difficult to debug which specific document is causing the issue.

### Reproduction

1. Create a docs folder with multiple markdown files
2. Introduce an error in one of the doc files (e.g., invalid frontmatter, broken metadata)
3. Try to build the site
4. The error message shows the version name but not which file caused the problem

### Expected behavior

The error message should include the file path (`path=...`) so we can quickly identify which document needs to be fixed. Previously this information was included in the error output.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This makes troubleshooting really tedious when you have dozens or hundreds of docs and need to hunt down which one has the issue.

---
Repository: /testbed
