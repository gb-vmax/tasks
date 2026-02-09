# Bug Report

### Describe the bug

There seems to be a syntax error in the OpenAPI 3 importer code that's preventing the application from running. After a recent update, I'm getting errors when trying to import OpenAPI 3 specifications.

### Reproduction

1. Try to import an OpenAPI 3 spec file
2. The import process fails immediately
3. Looking at the console, there appears to be a JavaScript syntax error in the openapi-3.ts importer

The issue seems to be in the `generateParameterExample` function where the code structure looks malformed - there's duplicate declarations and misplaced code that breaks the function definition.

### Expected behavior

The OpenAPI 3 importer should parse specification files correctly and generate appropriate parameter examples based on the schema types and formats (like email, date-time, byte, etc.).

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This is blocking my workflow as I can't import any OpenAPI specs at the moment. Would appreciate a quick fix!

---
Repository: /testbed
