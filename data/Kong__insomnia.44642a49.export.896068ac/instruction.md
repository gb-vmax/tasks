# Bug Report

### Describe the bug

The gRPC send button is now responding to keyboard shortcuts even when the method type is not set or invalid. When pressing Cmd+Enter (or Ctrl+Enter) without a valid method type selected, the button attempts to start a request which shouldn't be possible.

### Reproduction

```js
// Set up a gRPC request component
const grpcRequest = {
  methodType: undefined // or null
}

// Press Cmd+Enter or Ctrl+Enter
// Expected: Nothing should happen
// Actual: handleStart() is called even though there's no valid method type
```

Steps to reproduce:
1. Open a gRPC request in Insomnia
2. Don't select a method type (leave it empty/undefined)
3. Press Cmd+Enter (Mac) or Ctrl+Enter (Windows/Linux)
4. The send button tries to initiate a request

### Expected behavior

The keyboard shortcut should only work when a valid method type is selected. If `methodType` is undefined or null, pressing Cmd+Enter should not trigger `handleStart()`.

### Additional context

This seems to have started happening recently. The button text also shows "Cancel" when running without a method type, which is confusing since it should probably show something else or not be in a running state at all.

---
Repository: /testbed
