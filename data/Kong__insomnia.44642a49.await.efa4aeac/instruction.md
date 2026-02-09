# Bug Report

### Describe the bug

When a plugin hook throws an error, the error handling seems broken. The plugin information is not being attached to the error correctly, and in some cases the error might not be thrown at all.

### Reproduction

```js
// Create a plugin with a hook that throws an error
const plugin = {
  name: 'test-plugin',
  requestHooks: [
    (context) => {
      throw new Error('Something went wrong');
    }
  ]
};

// When the hook is executed, the error should have plugin info attached
// But the current behavior is inconsistent
```

### Expected behavior

When a plugin hook throws an error:
1. The error should be caught
2. The plugin information should be attached to the error object
3. The error should be re-thrown so it can be handled upstream

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
