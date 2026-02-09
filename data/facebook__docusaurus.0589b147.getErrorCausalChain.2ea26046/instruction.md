# Bug Report

### Describe the bug

The `getErrorCausalChain` function is returning an empty array when given an error without a cause, and the chain order appears reversed when errors do have causes. This breaks error handling and logging throughout the application.

### Reproduction

```js
const error = new Error('Something went wrong');
const chain = getErrorCausalChain(error);

console.log(chain);
// Expected: [Error: Something went wrong]
// Actual: []
```

For nested errors:
```js
const rootCause = new Error('Root cause');
const midError = new Error('Mid error', { cause: rootCause });
const topError = new Error('Top error', { cause: midError });

const chain = getErrorCausalChain(topError);

console.log(chain);
// Expected: [topError, midError, rootCause]
// Actual: [rootCause, midError, topError] (reversed order)
```

### Expected behavior

- When an error has no cause, the function should return an array containing just that error
- When an error has a causal chain, the array should be ordered from the top-level error down to the root cause
- The chain should never be empty when a valid error is passed in

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
