# Bug Report

### Describe the bug

When an error with a cause chain is logged, the last error in the chain is not being displayed. Only intermediate causes are shown, but the final cause in the chain gets skipped.

### Reproduction

```js
const rootCause = new Error('Root cause message');
const middleCause = new Error('Middle cause', { cause: rootCause });
const topError = new Error('Top level error', { cause: middleCause });

// When this error is handled, rootCause is not displayed
handleError(topError);
```

### Expected behavior

All errors in the cause chain should be displayed, including the final/root cause. The output should show:
- Top level error
- Middle cause  
- Root cause message

### Current behavior

Only the top level error and middle cause are shown. The root cause is missing from the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
