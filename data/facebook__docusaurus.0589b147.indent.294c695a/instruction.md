# Bug Report

### Describe the bug

The code generation for routes appears to have incorrect indentation. When generating route files, the indentation level seems to be off - everything is indented with 3 spaces instead of 2 spaces per level.

### Reproduction

When building a Docusaurus site, the generated route files have inconsistent indentation that doesn't match the expected 2-space indentation standard used throughout the codebase.

Steps to reproduce:
1. Build a Docusaurus site with multiple routes
2. Check the generated route configuration files
3. Notice that the indentation uses 3 spaces per level instead of 2

### Expected behavior

Generated route files should use consistent 2-space indentation to match the rest of the codebase and standard JavaScript/TypeScript formatting conventions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
