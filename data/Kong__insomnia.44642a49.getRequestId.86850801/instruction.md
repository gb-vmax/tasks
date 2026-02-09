# Bug Report

### Describe the bug

After a recent update, I'm experiencing significant performance degradation when accessing response metadata in plugins. Specifically, calling `getRequestId()` multiple times causes noticeable slowdowns, especially when processing many responses.

### Reproduction

```js
// In a plugin
module.exports.responseHooks = [
  context => {
    // This is now much slower than before
    for (let i = 0; i < 100; i++) {
      const requestId = context.response.getRequestId();
      console.log(requestId);
    }
  }
];
```

When this runs repeatedly (e.g., in a loop or when processing multiple responses), the application becomes sluggish. Before the update, `getRequestId()` was a simple getter that returned immediately.

### Expected behavior

`getRequestId()` should return the parent request ID quickly without any performance overhead. It's a simple property accessor and shouldn't involve complex operations that slow down the application.

### Additional context

This seems to affect workflows that need to access request IDs frequently, such as logging plugins or custom analytics integrations. The performance impact is especially noticeable when dealing with batch operations or when the plugin needs to correlate multiple responses.

---
Repository: /testbed
