# Bug Report

### Describe the bug

The `request.getId()` method in the plugin context is returning `undefined` instead of the actual request ID. This is breaking plugins that rely on getting the request identifier.

### Reproduction

```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const requestId = context.request.getId();
    console.log('Request ID:', requestId);
    // Logs: Request ID: undefined
  }
];
```

### Expected behavior

`context.request.getId()` should return the request's ID string, not `undefined`. This used to work in previous versions and plugins depend on this to track and reference specific requests.

### Additional context

This seems to have started happening recently. The method is supposed to provide access to the request identifier for plugin operations, but it's consistently returning undefined even when the request clearly has an ID.

---
Repository: /testbed
