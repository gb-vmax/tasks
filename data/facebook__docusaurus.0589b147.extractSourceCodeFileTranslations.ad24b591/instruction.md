# Bug Report

### Describe the bug

The translation extraction is failing silently when there are errors in source code files. Instead of properly reporting the issue, it just returns an empty object and continues processing. This makes it really hard to debug translation extraction problems.

### Reproduction

1. Create a source code file with translations that has a syntax error or parsing issue
2. Run the translation extraction process
3. The extraction completes without any error being thrown
4. The translations from that file are silently missing from the output

### Expected behavior

When there's an error extracting translations from a source code file, the error should be thrown after logging so that the build process fails and the developer is aware of the issue. Silent failures make it impossible to know that translations are missing.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
