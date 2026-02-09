# Bug Report

### Describe the bug
The `getId()` method in the plugin context is throwing errors when called without arguments. After a recent update, calling `request.getId()` fails with an error about invalid request IDs, even though the request object is valid and has a proper ID.

### Reproduction
```js
// In a plugin script
const requestId = request.getId();
console.log(requestId); // Should print the request ID
```

This throws an error:
```
Invalid request ID: ID must be a non-empty string
```

The same issue occurs when trying to use the method in request hooks or custom plugins. It seems like the method is now expecting the ID to be validated in a way that breaks existing functionality.

### Expected behavior
`request.getId()` should return the request ID without throwing an error, just like it did in previous versions. The method should work when called with no arguments.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking all of my existing plugins that rely on getting the request ID. Any help would be appreciated!

---
Repository: /testbed
