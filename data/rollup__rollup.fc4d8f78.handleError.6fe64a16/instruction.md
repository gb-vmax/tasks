# Bug Report

### Describe the bug

When an error with a `cause` property is logged, the error cause chain is not being fully displayed. Only nested causes (cause of cause) are shown, but the immediate first-level cause is missing from the output.

### Reproduction

```js
const innerError = new Error('Root cause');
const middleError = new Error('Middle error');
middleError.cause = innerError;
const outerError = new Error('Outer error');
outerError.cause = middleError;

// When this error is handled, the middleError information is lost
handleError(outerError);
```

### Expected behavior

All error causes in the chain should be displayed, including the immediate cause of the error. The output should show:
1. The outer error
2. The middle error (first cause)
3. The inner error (cause of cause)

Currently, only the outer error and inner error are displayed, with the middle error being skipped.

### Additional context

This seems to affect error reporting where understanding the full error chain is important for debugging. The immediate cause of an error is often the most relevant piece of information for troubleshooting.

---
Repository: /testbed
