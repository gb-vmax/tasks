# Bug Report

### Describe the bug

When using the plugin API to send network requests via `context.network.sendRequest()`, the function appears to be incomplete or broken. The request never completes and seems to hang indefinitely.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    context.hooks.afterResponse = async (context) => {
      // Try to send a follow-up request
      const response = await context.network.sendRequest(someRequest);
      // This never returns
    };
  }
];
```

### Steps to reproduce:
1. Create a plugin that uses `context.network.sendRequest()`
2. Call the method with a valid request object
3. The function hangs and never resolves

### Expected behavior

The `sendRequest()` method should complete the network request and return a response object as it did in previous versions.

### Additional context

This seems to have started happening recently. The method used to work fine but now requests just hang. Not sure if this is related to any recent changes to the network layer or plugin context.

---
Repository: /testbed
