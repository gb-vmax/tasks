# Bug Report

### Describe the bug

After recent changes, requests are not being updated properly in the application. When I modify a request (e.g., changing URL, headers, or body), the changes don't seem to persist or reflect correctly in the UI. The old cached values appear to be displayed instead of the updated ones.

### Reproduction

```js
// Get a request
const request = await getById('req_123');

// Update the request
await update(request, { url: 'https://new-url.com' });

// Get the same request again
const updatedRequest = await getById('req_123');

// The URL is still the old value, not 'https://new-url.com'
console.log(updatedRequest.url); // Shows old URL instead of new one
```

### Expected behavior

When a request is updated using the `update()` function, subsequent calls to `getById()` should return the updated request data with the new values, not stale cached data.

### Additional context

This seems to affect all request types (regular requests, gRPC requests, and WebSocket requests). The issue appears intermittently but becomes more noticeable when making multiple updates in quick succession.

---
Repository: /testbed
