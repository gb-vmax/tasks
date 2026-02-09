# Bug Report

### Describe the bug

After a recent update, response bodies are not being returned correctly. When making requests, I'm getting empty responses even though the request completes successfully and the response body should contain data.

### Reproduction

```js
// Make a request that should return a response body
const response = await sendRequest(request);

// Try to access the response body
const body = getBodyBuffer(response);

// Expected: Buffer with actual response data
// Actual: Empty buffer or null
```

The issue seems to happen consistently - response bodies that should contain data are coming back empty. The `bodyPath` is set correctly on the response object, but `getBodyBuffer()` isn't returning the expected data.

### Expected behavior

`getBodyBuffer()` should return the actual response body content when a valid `bodyPath` is provided in the response object. Previously this was working fine, but now it appears to be broken.

### Additional context

This is blocking our ability to view response data in the UI. The requests themselves seem to be working (status codes are correct), but we can't see the actual response content anymore.

---
Repository: /testbed
