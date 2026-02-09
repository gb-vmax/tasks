# Bug Report

### Describe the bug

The `util.models.request.getById()` function in template tag extensions is returning `null` for valid requests when the request status is `'pending'`. This is causing template tags that rely on fetching request data to fail unexpectedly.

### Reproduction

```js
// In a custom template tag
const requestId = 'valid-request-id-123';
const request = await context.util.models.request.getById(requestId);

// request is null even though the request exists
console.log(request); // null

// This happens when the request has status: 'pending'
```

### Expected behavior

The function should return the request object regardless of its status. If a request exists with the given ID, it should be returned. The status field should not affect whether the request is retrievable.

### Additional context

This seems to have started happening recently. Previously, `getById()` would return requests with any status. Now it's filtering out pending requests which breaks workflows that need to access request data during the pending state.

---
Repository: /testbed
