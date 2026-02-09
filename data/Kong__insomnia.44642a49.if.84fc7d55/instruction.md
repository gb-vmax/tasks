# Bug Report

### Describe the bug

After a recent update, request operations are behaving inconsistently. When fetching requests by ID, the system sometimes returns stale data instead of the most current version. This is particularly noticeable when a request is modified and then immediately retrieved - the old version is returned instead of the updated one.

### Reproduction

```js
// 1. Get a request
const request = await getById('req_123');
console.log(request.name); // "Original Name"

// 2. Update the request in the database
await updateRequest('req_123', { name: 'Updated Name' });

// 3. Fetch the same request again
const updatedRequest = await getById('req_123');
console.log(updatedRequest.name); // Still shows "Original Name" instead of "Updated Name"
```

### Expected behavior

The `getById` function should always return the most current version of a request from the database, not a cached or stale version.

### Additional context

This seems to affect all request types (regular requests, gRPC requests, and WebSocket requests). The issue is intermittent but happens frequently enough to be problematic in workflows where requests are being modified and then immediately accessed.

---
Repository: /testbed
