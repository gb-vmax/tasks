# Bug Report

### Describe the bug
When trying to view response bodies in the application, I'm getting empty responses even when the server returns data. It seems like the response body is being replaced with an empty buffer instead of showing the actual content.

### Reproduction
```js
// Make any API request that returns a response body
// For example, a GET request to an endpoint that returns JSON

// Expected: Response body shows the JSON data
// Actual: Response body is empty
```

Steps to reproduce:
1. Create a new request to any endpoint that returns data
2. Send the request
3. Check the response body viewer
4. The body appears empty even though the server sent data

### Expected behavior
When a response has a body with content, it should be displayed in the response viewer. The body should only be empty when the server actually returns no content.

### Additional context
This seems to affect all requests with response bodies. Responses that legitimately have no body (like 204 No Content) might be working correctly, but I can't tell since everything is showing as empty now.

---
Repository: /testbed
