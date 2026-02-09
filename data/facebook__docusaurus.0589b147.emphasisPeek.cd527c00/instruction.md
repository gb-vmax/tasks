# Bug Report

### Describe the bug

Getting a `TypeError: Cannot read properties of undefined (reading 'emphasis')` when using the remark markdown processor. This seems to happen when the state object doesn't have an options property initialized.

### Reproduction

```js
const state = {
  // options is not set
};

// Trying to access emphasis option causes error
const result = emphasisPeek(null, null, state);
```

The error occurs because the code tries to access `state.options.emphasis` without checking if `state.options` exists first.

### Expected behavior

The function should handle cases where `state.options` is undefined and fall back to the default value (`"*"`) without throwing an error.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
