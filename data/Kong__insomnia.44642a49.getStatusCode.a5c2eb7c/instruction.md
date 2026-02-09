# Bug Report

### Describe the bug

After a recent update, the `getStatusCode()` method in the response context is no longer working in my plugin scripts. When I try to access the status code from a response object, I'm getting an error or undefined behavior.

### Reproduction

```js
// In a plugin script
const statusCode = insomnia.response.getStatusCode();
console.log(statusCode); // This fails or returns unexpected results
```

I have several plugin scripts that rely on checking the HTTP status code to determine if a request was successful, and they all stopped working after updating.

### Expected behavior

The `getStatusCode()` method should return the HTTP status code (e.g., 200, 404, 500) as it did before. My plugins use this to implement conditional logic based on response status.

### Additional context

This is breaking my workflow as I have automation scripts that check status codes to decide whether to proceed with subsequent requests. The method was working fine in the previous version.

---
Repository: /testbed
