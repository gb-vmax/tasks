# Bug Report

### Describe the bug

When a request plugin hook throws an error, the error information is being lost. Specifically, the `plugin` property that was attached to the error is no longer available, making it difficult to debug which plugin caused the issue.

### Reproduction

```js
// Create a plugin with a hook that throws an error
const myPlugin = {
  requestHooks: [
    async (context) => {
      throw new Error('Something went wrong in my plugin');
    }
  ]
};

// Try to execute the request
// The error thrown will not contain information about which plugin failed
```

### Expected behavior

When a plugin hook throws an error, the error should maintain its original properties including the `plugin` reference so developers can identify which plugin is causing issues. The error object should preserve all diagnostic information to help with debugging.

### Additional context

This makes it really hard to track down which plugin is causing problems when multiple plugins are installed. Previously the error would include plugin metadata but now it's just a generic error message.

---
Repository: /testbed
