# Bug Report

### Describe the bug

When using `request.getId()` in a plugin context, it returns `undefined` instead of the actual request ID. This breaks any plugin that relies on getting the request identifier.

### Reproduction

```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const id = context.request.getId();
    console.log('Request ID:', id); // Prints: Request ID: undefined
  }
];
```

### Expected behavior

`request.getId()` should return the request's unique identifier string, not `undefined`.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently - plugins that were working before are now failing to get request IDs properly.

---
Repository: /testbed
