# Bug Report

### Describe the bug

I'm experiencing an issue with plugin hooks in the request pipeline. When a plugin hook is executed, the application seems to hang or become unresponsive. It looks like the hook execution is getting stuck somewhere and never completes.

### Reproduction

```js
// Register a plugin with a request hook
const plugin = {
  requestHooks: [
    async (context) => {
      // Perform some async operation
      await someAsyncOperation(context.request);
    }
  ]
};

// When the request is sent, the application hangs
// and the request never completes
```

### Steps to reproduce:
1. Create a plugin with a request hook that performs an async operation
2. Send a request that triggers the plugin hook
3. The application becomes unresponsive and the request never completes

This is blocking me from using plugins that need to make external API calls or perform any async work during request processing. The hook seems to run indefinitely without any timeout mechanism.

### Expected behavior

The plugin hook should execute and complete (or fail with a timeout error) so that the request can proceed. There should be some mechanism to prevent hooks from hanging indefinitely.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
