# Bug Report

### Describe the bug

After a recent update, the application fails to start and crashes immediately. Looking at the code, it seems like there's a syntax error or incomplete code in the request-operations module that's preventing the application from loading.

### Reproduction

1. Pull the latest changes
2. Try to start the application
3. Application crashes on startup

The issue appears to be in `packages/insomnia/src/models/helpers/request-operations.ts` - the code seems to be cut off or incomplete at the end of the file.

### Expected behavior

The application should start normally without any syntax errors.

### System Info
- Version: latest from main branch
- OS: Any

This is blocking our ability to use the application at all. Would appreciate a quick fix!

---
Repository: /testbed
