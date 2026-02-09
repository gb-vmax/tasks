# Bug Report

### Describe the bug

After a recent update, the application fails to start and crashes immediately with a syntax error. The error appears to be related to the merge conflict schema definitions in the sync module.

### Reproduction

1. Pull the latest changes
2. Try to start the application
3. Application crashes on startup

The issue seems to be in the `type-schemas.ts` file where the merge conflict schema is defined. The code structure appears malformed - there's a function definition that's not properly integrated into the object structure.

### Expected behavior

The application should start normally without any syntax errors. The merge conflict schema should be properly defined with all its properties accessible.

### System Info
- Node version: Latest
- OS: Any

This is blocking our workflow as the app won't even launch. Any help would be appreciated!

---
Repository: /testbed
