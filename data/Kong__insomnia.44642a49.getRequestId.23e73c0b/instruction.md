# Bug Report

### Describe the bug

When using the plugin API to get the request ID from a response context, `getRequestId()` is returning `null` instead of an empty string when the parent ID is not set. This breaks plugins that expect a string value and causes runtime errors when trying to use string methods on the returned value.

### Reproduction

```js
// In a plugin
const response = context.response;
const requestId = response.getRequestId();

// This now throws an error when parentId is not set
const uppercaseId = requestId.toUpperCase(); // TypeError: Cannot read property 'toUpperCase' of null
```

### Expected behavior

`getRequestId()` should return an empty string (`''`) when there is no parent ID, not `null`. This maintains backward compatibility with existing plugins that expect a string return type.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
