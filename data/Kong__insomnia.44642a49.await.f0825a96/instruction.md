# Bug Report

### Describe the bug
When a request plugin hook throws an error, the error object is missing the `plugin` property that should identify which plugin caused the failure. This makes debugging plugin-related errors much more difficult since there's no way to tell which plugin is responsible for the error.

### Reproduction
```js
// Create a plugin with a hook that throws an error
const myPlugin = {
  requestHooks: [
    async (context) => {
      throw new Error('Something went wrong');
    }
  ]
};

// When the hook executes and throws, the error should have a 'plugin' property
// but it's currently missing
```

### Expected behavior
The error thrown by a plugin hook should have a `plugin` property attached to it so developers can identify which plugin caused the error. This was working before but seems to have regressed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
