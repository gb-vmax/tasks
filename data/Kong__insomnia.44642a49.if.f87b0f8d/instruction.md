# Bug Report

### Describe the bug

After a recent update, the `getById` function in `request-operations.ts` appears to be broken. When trying to fetch requests by ID, the function returns `null` or doesn't return at all. This is affecting the ability to load and display requests in the UI.

### Reproduction

```js
// Attempting to get a WebSocket request by ID
const requestId = 'wrk_abc123';
const request = await getById(requestId);

// Expected: WebSocketRequest object
// Actual: null or function hangs
```

Steps to reproduce:
1. Try to fetch any request using `getById()` with a valid request ID
2. The function fails to return the expected request object
3. WebSocket requests seem particularly affected

### Expected behavior

The `getById` function should correctly retrieve and return the request object (Request, GrpcRequest, or WebSocketRequest) when given a valid request ID. It should work for all request types without hanging or returning null unexpectedly.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't load existing requests anymore. Any help would be appreciated!

---
Repository: /testbed
