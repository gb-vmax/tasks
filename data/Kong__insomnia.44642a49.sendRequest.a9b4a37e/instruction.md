# Bug Report

### Describe the bug

After a recent update, the plugin network API seems to have broken. When I try to use `sendRequest()` from a plugin, I'm getting syntax errors and the request doesn't execute at all.

### Reproduction

```js
module.exports.requestHooks = [
  context => {
    context.request.addHeader('X-Custom', 'value');
  }
];

module.exports.responseHooks = [
  async context => {
    // Try to send another request
    const response = await context.network.sendRequest(someRequest);
    console.log(response);
  }
];
```

When the plugin tries to call `sendRequest`, the entire request fails and nothing happens. It looks like the function is incomplete or corrupted somehow.

### Expected behavior

The `sendRequest()` method should work as before, sending the request and returning a response object. Plugins should be able to programmatically trigger additional requests.

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine in the previous version. Seems like something got broken in the network context implementation.

---
Repository: /testbed
