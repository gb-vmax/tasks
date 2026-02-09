# Bug Report

### Describe the bug
When a plugin hook throws an error, the original error's stack trace is being lost. Only the error message is preserved, making it extremely difficult to debug plugin issues since we can't see where the error actually originated from.

### Reproduction
```js
// In a plugin hook
const myPlugin = {
  requestHooks: [
    async (context) => {
      // This will throw an error with a stack trace
      throw new Error('Something went wrong in the plugin');
    }
  ]
};

// When the hook is executed, the error is caught and re-thrown
// but the stack trace information is lost
```

### Expected behavior
The full error object including the stack trace should be preserved when re-throwing plugin errors. This is critical for debugging because:
1. We need to know the exact line where the error occurred
2. We need the full call stack to understand the error context
3. Creating a new Error object only with the message loses all this information

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
