# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use gRPC requests. The application fails to load and throws an error related to the grpc-request-meta module.

### Reproduction

1. Start the application
2. Try to access any gRPC request functionality
3. Application crashes with a syntax error

The error seems to be coming from the `grpc-request-meta.ts` file. When I check the file, it looks like there's incomplete code at the end - the `getByParentId` function appears to be cut off mid-word with `expec`.

### Expected behavior

The application should start normally and gRPC requests should be accessible without any syntax errors.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This is blocking me from using any gRPC functionality. Would appreciate a quick fix!

---
Repository: /testbed
