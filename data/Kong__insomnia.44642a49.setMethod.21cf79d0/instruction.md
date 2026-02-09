# Bug Report

### Describe the bug

After a recent update, the `setMethod()` function in the plugin context is not working properly. When I try to set the HTTP method using this function, it seems to be doing unexpected things with headers that weren't happening before.

### Reproduction

```js
// In a plugin script
const method = request.getMethod(); // Returns 'GET'
request.setMethod('POST');

// Expected: Method changes to 'POST'
// Actual: Method changes but headers are also being modified unexpectedly
```

I'm also seeing issues when switching between different HTTP methods - sometimes headers disappear or get added when they shouldn't be touched at all. The function used to just change the method and nothing else.

### Expected behavior

The `setMethod()` function should only change the HTTP method of the request, without modifying any headers or other request properties. If I want to manage headers, I should do that separately.

### System Info
- Insomnia version: latest
- Plugin API context: request

Has anyone else run into this? The old behavior was much simpler and more predictable.

---
Repository: /testbed
