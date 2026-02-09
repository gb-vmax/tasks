# Bug Report

### Describe the bug

When making requests that result in errors, the SDK is returning `undefined` instead of a proper Response object. This makes it impossible to handle error cases in scripts, as there's no way to access error information or determine what went wrong with the request.

### Reproduction

```js
// Make a request that will fail (e.g., network error, timeout, invalid URL)
const response = await insomnia.send(request);

// response is undefined instead of containing error information
console.log(response); // undefined
```

Expected to be able to access error details like:
- Error message
- Error code
- Status information
- Error type

### Expected behavior

The SDK should return a Response object even when errors occur, containing the error information in a structured format (headers, body, etc.) so that scripts can properly handle failures.

### System Info
- Insomnia SDK version: latest
- Platform: All

---
Repository: /testbed
