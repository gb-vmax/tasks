# Bug Report

### Describe the bug
When using `request.getId()` in plugins, the returned ID is missing the first character. This breaks plugin functionality that relies on matching request IDs with other parts of the application.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const requestId = context.request.getId();
    console.log('Request ID:', requestId);
    // Expected: "req_abc123"
    // Actual: "eq_abc123" (first character missing)
  }
];
```

### Expected behavior
`request.getId()` should return the complete request ID including all characters, matching the ID used elsewhere in the application.

### System Info
- Insomnia version: latest
- Platform: All platforms

This appears to have started recently and is causing issues with plugins that need to reference requests by ID.

---
Repository: /testbed
