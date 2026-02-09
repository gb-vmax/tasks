# Bug Report

### Describe the bug

After a recent update, I'm unable to retrieve the latest response for a request. The application throws an error when trying to access response history, and it seems like the `getLatestForRequest` function has been removed or is no longer available.

### Reproduction

```js
// This used to work but now fails
const latestResponse = await getLatestForRequest(requestId, environmentId);

// Error: getLatestForRequest is not defined
```

Steps to reproduce:
1. Make a request and save the response
2. Try to retrieve the latest response using `getLatestForRequest()`
3. Function is undefined/not exported

### Expected behavior

The `getLatestForRequest` function should be available and return the most recent response for a given request ID and environment ID. This was working in previous versions.

### Additional context

It looks like the response model was refactored and some functions might have been accidentally removed. The `create` function also appears to be incomplete in the current version - the code seems to cut off mid-statement.

---
Repository: /testbed
