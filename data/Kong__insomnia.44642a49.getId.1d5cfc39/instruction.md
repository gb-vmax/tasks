# Bug Report

### Describe the bug
When using the plugin context API to access request information, `request.getId()` returns `undefined` instead of the expected request ID. This breaks plugins that rely on getting the request ID to perform operations or track requests.

### Reproduction
```js
// In a plugin hook
const requestId = context.request.getId();
console.log(requestId); // prints undefined instead of the actual ID
```

The issue occurs when trying to retrieve the request ID through the plugin context. The method returns `undefined` even though the request object exists and has a valid `_id` property.

### Expected behavior
`request.getId()` should return the request's ID string, not `undefined`. This worked correctly in previous versions and is needed for plugins to properly identify and work with requests.

### Additional context
This seems to have started happening recently. Plugins that were working before are now failing because they can't get the request ID anymore.

---
Repository: /testbed
