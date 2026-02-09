# Bug Report

### Describe the bug

After a recent update, the plugin response context is returning stale/cached body data when the response body changes. When making multiple requests to the same endpoint with different response bodies, the `getBody()` method sometimes returns the body from a previous request instead of the current one.

### Reproduction

```js
// Make first request
const response1 = await context.request.send(requestId);
const body1 = response1.getBody();
console.log(body1); // Shows correct body for first request

// Make second request to same endpoint (different response)
const response2 = await context.request.send(requestId);
const body2 = response2.getBody();
console.log(body2); // Shows body from first request instead of second
```

### Steps to reproduce:
1. Create a plugin that calls `response.getBody()` 
2. Make a request to an endpoint
3. Make another request to the same endpoint that returns different content
4. The second call to `getBody()` returns the cached body from the first request

### Expected behavior

Each call to `getBody()` should return the actual body content for that specific response, not a cached version from a previous response.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
