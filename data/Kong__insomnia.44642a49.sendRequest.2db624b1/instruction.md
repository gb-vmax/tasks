# Bug Report

### Describe the bug

After a recent update, the plugin network context appears to be broken. When trying to send requests through plugins using `context.network.sendRequest()`, I'm getting errors about incomplete or malformed code. The request never actually gets sent.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    context.request.addHeader('X-Custom', 'test');
  }
];

module.exports.responseHooks = [
  async context => {
    // Try to send a follow-up request
    const response = await context.network.sendRequest(someRequest);
    // This fails with a syntax error
  }
];
```

### Expected behavior

The `sendRequest()` method should successfully send the request and return a response object as it did before. Plugins should be able to make network requests without errors.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we rely on plugins to send follow-up requests based on initial responses. Any help would be appreciated!

---
Repository: /testbed
