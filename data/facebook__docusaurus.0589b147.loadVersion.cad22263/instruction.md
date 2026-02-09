# Bug Report

### Describe the bug

When a version fails to load in the docs plugin, the error is being silently swallowed instead of being propagated. The error message also shows incorrect information - it says "Loading of version completed" when it actually failed, and it references `versionPath` instead of `versionName`.

### Reproduction

1. Set up a docs plugin with multiple versions
2. Introduce an error in one of the version configurations (e.g., invalid markdown, missing files, etc.)
3. Build the site
4. The build completes successfully even though a version failed to load
5. The error log shows "Loading of version completed" which is misleading

### Expected behavior

- When a version fails to load, the error should be thrown and the build should fail
- The error message should accurately reflect that loading failed (not "completed")
- The error message should reference the correct property (`versionName` not `versionPath`)

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like a regression that could cause silent failures in production builds where version loading errors go unnoticed.

---
Repository: /testbed
