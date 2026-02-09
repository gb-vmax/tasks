# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to duplicate requests in Insomnia. It appears that the code for handling request duplication has been corrupted or improperly formatted, causing the application to fail when attempting to duplicate any type of request (HTTP, gRPC, or WebSocket).

### Reproduction

1. Open Insomnia
2. Create any type of request (HTTP, gRPC, or WebSocket)
3. Right-click on the request and select "Duplicate"
4. The application fails to duplicate the request

The issue seems to be in the request-operations.ts file where the duplicate function has malformed code structure. There appears to be duplicate function definitions and helper functions defined in the wrong scope.

### Expected behavior

Duplicating a request should create a copy of the original request with a new ID and updated metadata. The duplicate function should properly handle all request types (HTTP, gRPC, WebSocket) and sanitize the patch object before creating the duplicate.

### System Info
- Insomnia version: Latest
- OS: Any

This looks like it might have been introduced in a recent code change where refactoring wasn't completed properly. The function signature appears twice and there are helper functions that seem to be in the wrong location.

---
Repository: /testbed
