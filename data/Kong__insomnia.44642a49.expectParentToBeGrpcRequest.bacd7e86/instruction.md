# Bug Report

### Describe the bug

I'm encountering an issue where GrpcRequestMeta validation is failing with an unclear error message. When trying to work with gRPC requests that have invalid parent IDs, the error doesn't provide enough context about what value was actually received.

### Reproduction

```js
// Attempting to create or update a GrpcRequestMeta with an invalid parent
const meta = {
  parentId: null, // or undefined, or empty string
  // ... other properties
}

// This throws an error but doesn't tell me what the actual value was
```

The current error message just says "Expected the parent of GrpcRequestMeta to be a GrpcRequest" without showing what was actually provided.

### Expected behavior

The error message should include:
- The actual value that was received (e.g., null, undefined, empty string)
- The type of the value
- More context to help debug the issue

This would make it much easier to track down where invalid parent IDs are coming from in the application.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
