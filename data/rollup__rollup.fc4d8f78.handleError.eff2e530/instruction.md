# Bug Report

### Describe the bug

When an error has a nested `cause` chain, the error message displayed is incorrect. The logging system seems to be skipping the immediate cause and jumping to the nested cause, which results in confusing error messages being shown to users.

### Reproduction

```js
const innerError = new Error('Inner error message');
const middleError = new Error('Middle error message');
middleError.cause = innerError;
const outerError = new Error('Outer error message');
outerError.cause = middleError;

// When this error is handled, the message shows "Middle error message" 
// instead of "Outer error message"
handleError(outerError);
```

### Expected behavior

The error handler should display the message from the actual error being handled, not from its cause. In the example above, it should show "Outer error message" first, and then optionally show the cause chain below.

### Additional context

This appears to be affecting error reporting in the CLI, making it difficult to understand what actually went wrong when errors have a cause chain. The displayed error message doesn't match the top-level error that was thrown.

---
Repository: /testbed
