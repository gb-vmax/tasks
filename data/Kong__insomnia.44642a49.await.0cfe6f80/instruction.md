# Bug Report

### Describe the bug

Request plugin hooks are not being awaited properly, which causes async plugin operations to be skipped or not complete before the request continues processing. This results in plugins that perform asynchronous operations (like fetching tokens, modifying headers, etc.) to not work correctly.

### Reproduction

```js
// Create a plugin with an async hook
const myPlugin = {
  requestHooks: [
    async (context) => {
      // Simulate async operation (e.g., fetching auth token)
      await new Promise(resolve => setTimeout(resolve, 100));
      context.request.setHeader('Authorization', 'Bearer token123');
    }
  ]
};

// When the request is sent, the Authorization header is missing
// because the async operation wasn't completed
```

### Expected behavior

Plugin hooks should wait for async operations to complete before continuing with request processing. Headers, body modifications, or any other changes made by async plugin hooks should be applied to the request.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
