# Bug Report

### Describe the bug

I'm encountering an issue with the markdown serialization when using the `strongPeek` function. It appears that accessing `state.options.strong` causes an error when `state.options` is undefined or null, leading to a crash in the markdown processing.

### Reproduction

```js
// When state.options is undefined/null
const state = {
  options: undefined
};

// Calling strongPeek results in an error
strongPeek(null, null, state);
// Expected to return a fallback value, but throws TypeError
```

This happens when processing markdown with strong emphasis markers (bold text) in certain edge cases where the state object doesn't have options properly initialized.

### Expected behavior

The function should handle cases where `state.options` is undefined or null gracefully, returning an appropriate fallback value (like "*") instead of throwing an error.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
