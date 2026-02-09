# Bug Report

### Describe the bug

When trying to retrieve the latest response for a request, I'm getting `undefined` instead of the expected response object. This seems to happen consistently after a recent update.

### Reproduction

```js
const requestId = 'req_123';
const environmentId = 'env_456';

// This returns undefined even though responses exist
const latestResponse = await getLatestForRequest(requestId, environmentId);
console.log(latestResponse); // undefined
```

### Expected behavior

`getLatestForRequest()` should return the most recent response object for the given request ID and environment ID, or `null` if no responses exist.

### Additional context

I noticed this started happening recently. The function seems to have been removed or refactored but I can't find a replacement method in the API. Other response-related functions like `remove()` still work fine.

Is there a new way to get the latest response that I should be using instead?

---
Repository: /testbed
