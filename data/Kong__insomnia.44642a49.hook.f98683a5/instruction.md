# Bug Report

### Describe the bug

The default headers functionality appears to be broken after a recent update. When setting `DEFAULT_HEADERS` in environment variables, the headers are no longer being applied to requests.

### Reproduction

```js
// Set up environment variable
const env = {
  DEFAULT_HEADERS: {
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json'
  }
}

// Make a request
// Expected: Headers should be automatically added
// Actual: Headers are not being set
```

I've been using the `DEFAULT_HEADERS` environment variable to automatically add common headers to all my requests, but this stopped working. The headers are simply not being applied anymore.

### Expected behavior

When `DEFAULT_HEADERS` is defined in the environment variables, those headers should be automatically added to requests that don't already have them set. Previously this was working fine - I could define default headers once and they would be applied across all requests.

### Additional context

This was working in the previous version. The hook that processes default headers seems to have been removed or refactored in a way that breaks the existing functionality. 

My workflow relies heavily on this feature to avoid manually setting the same headers on every single request.

---
Repository: /testbed
