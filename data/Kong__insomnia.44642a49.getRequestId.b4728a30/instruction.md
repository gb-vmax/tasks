# Bug Report

### Describe the bug
After a recent update, the `getRequestId()` method in the plugin context is returning unexpected values. It appears to be stripping prefixes from request IDs, which is breaking plugins that rely on the full request ID format.

### Reproduction
```js
// In a plugin that uses the response context
module.exports.responseHooks = [
  context => {
    const requestId = context.response.getRequestId();
    console.log('Request ID:', requestId);
    // Expected: "req_abc123" 
    // Actual: "abc123" (prefix stripped)
  }
];
```

### Steps to reproduce:
1. Create a plugin that accesses `context.response.getRequestId()`
2. Make a request with ID like "req_abc123" or "wrk_def456"
3. The returned ID has the prefix removed

### Expected behavior
The method should return the complete request ID including any prefixes (req_, wrk_, fol_, etc.) to maintain backwards compatibility with existing plugins. Our plugin uses the full ID to match against stored data and this change breaks that functionality.

### Additional context
This is causing issues with plugins that store or compare request IDs, as they now receive IDs in a different format than what was originally stored. Would appreciate if this could be reverted or at least made opt-in via a parameter.

---
Repository: /testbed
