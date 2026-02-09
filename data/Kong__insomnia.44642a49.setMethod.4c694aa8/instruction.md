# Bug Report

### Describe the bug

After a recent update, the `setMethod()` function in the plugin context is automatically clearing the request body when switching to certain HTTP methods. This is causing issues when I need to preserve body data while changing methods.

### Reproduction

```js
const request = context.request;

// Set up a request with a body
request.setMethod('POST');
request.setBody({ 
  mimeType: 'application/json',
  text: '{"key": "value"}'
});

// Switch to DELETE method
request.setMethod('DELETE');

// Body is now unexpectedly cleared!
// Expected: Body should remain intact
// Actual: Body is set to { mimeType: '', text: '' }
```

### Expected behavior

The `setMethod()` function should only update the HTTP method without touching other request properties like the body. If I want to clear the body, I should do that explicitly.

Some APIs actually do accept request bodies with DELETE, GET, and other methods even though it's not common practice. The plugin shouldn't make assumptions about what's valid for my use case.

### Additional context

This seems to happen specifically when switching to GET, HEAD, DELETE, or OPTIONS methods. The body gets automatically cleared which breaks my workflow where I need to preserve the body content across method changes.

---
Repository: /testbed
