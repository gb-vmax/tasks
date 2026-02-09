# Bug Report

### Describe the bug

I'm encountering an issue with translation extraction warnings where the reported line numbers are incorrect. When a translation warning is generated, it points to the wrong line in the source file, making it difficult to locate the actual problematic code.

### Reproduction

When using the `translate` API in a component and triggering a warning (e.g., missing translation ID or malformed usage), the warning message shows an incorrect line number that doesn't match where the code actually is in the file.

For example, if the problematic code is on line 10, the warning might report line 15 or some other incorrect line number. This makes debugging translation issues much harder than it should be.

### Expected behavior

The warning should report the correct line number where the translation call appears in the source code, so developers can quickly locate and fix the issue.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
