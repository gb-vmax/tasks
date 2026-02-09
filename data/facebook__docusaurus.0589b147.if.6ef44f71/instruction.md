# Bug Report

### Describe the bug

Git history retrieval is failing even when git is properly installed on the system. The error message says "git command execution failed" but git is available and working correctly.

### Reproduction

1. Make sure git is installed and available in PATH (`git --version` works)
2. Try to build a Docusaurus site that uses git history features (e.g., last update time for docs)
3. Build fails with error: `Failed to retrieve git history for "<file>" because git command execution failed.`

This seems to have started happening recently. The error occurs even though git is definitely installed and accessible from the command line.

### Expected behavior

The build should succeed and retrieve git history information when git is installed. The error should only be thrown when git is actually not available.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: Ubuntu 22.04
- Git version: 2.34.1

---
Repository: /testbed
