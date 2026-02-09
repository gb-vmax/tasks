# Bug Report

### Describe the bug

The `removeParameter()` function is not working correctly after a recent update. When I try to remove a parameter by its exact name, nothing happens and the parameter remains in the request.

### Reproduction

```js
// Set up a request with parameters
request.setParameter('api_key', '12345');
request.setParameter('user_id', '67890');

// Try to remove a specific parameter
request.removeParameter('api_key');

// Expected: api_key should be removed
// Actual: api_key is still present in the request parameters
```

### Expected behavior

When calling `removeParameter()` with an exact parameter name (like `'api_key'`), that parameter should be removed from the request. The function worked fine before but now it seems like parameters aren't being removed unless I use wildcard patterns.

### Additional context

I noticed this started happening recently. I'm just trying to remove a single parameter by name, not using any glob patterns or wildcards. The parameter stays in the request even after calling `removeParameter()`.

---
Repository: /testbed
