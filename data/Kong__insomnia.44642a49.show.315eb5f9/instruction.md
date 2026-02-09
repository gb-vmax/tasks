# Bug Report

### Describe the bug

I'm experiencing an issue with the AskModal component where the code appears to be incomplete or corrupted. The modal's `show` method seems to have been improperly modified and the code is cut off mid-statement.

### Reproduction

When trying to use the AskModal component, the application fails to compile or throws syntax errors. Looking at the source code, the `show` method definition appears to be malformed:

```tsx
// The show method seems to have code that's not properly structured
show: ({ title, message, onDone, yesText, noText, color, timeout }) => {
  // ... some logic here
  // but then it just cuts off with:
  clearInterv
```

The method definition doesn't close properly and appears to end abruptly with an incomplete `clearInterval` call.

### Expected behavior

The AskModal component should compile and work correctly. The `show` method should be properly defined with complete function bodies and all code blocks properly closed.

### Additional context

This seems to have broken after recent changes to add timeout/countdown functionality to the modal. The new helper functions `handleButtonClick` and `getButtonText` are defined but appear to be in the wrong scope (inside the `show` method definition instead of at the component level).

---
Repository: /testbed
