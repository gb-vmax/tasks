# Bug Report

### Describe the bug
When creating a new gRPC request, the initial body text is empty instead of containing a default empty JSON object. This causes issues when trying to send requests immediately after creation, as the body is not valid JSON.

### Reproduction
```js
const grpcRequest = init();

// Expected: grpcRequest.body.text === '{}'
// Actual: grpcRequest.body.text === ''
```

### Steps to reproduce:
1. Create a new gRPC request using the init() function
2. Check the body.text property
3. The body is an empty string instead of '{}'

### Expected behavior
The body.text should be initialized with '{}' (empty JSON object) by default, so that requests have valid JSON from the start without requiring manual initialization.

### Additional context
This is particularly problematic when users try to send a gRPC request immediately after creation, as the empty string is not valid JSON and will cause parsing errors.

---
Repository: /testbed
