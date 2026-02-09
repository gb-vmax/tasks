# Bug Report

### Describe the bug

The `getErrorCausalChain` function is returning incorrect results when processing error chains. When I pass an error object to this function, it's not returning the complete causal chain as expected.

### Reproduction

```js
const error1 = new Error('Root cause');
const error2 = new Error('Secondary error');
error2.cause = error1;

const chain = getErrorCausalChain(error2);
console.log(chain);
// Expected: [error2, error1]
// Actual: []
```

Also, when using errors without a cause:

```js
const singleError = new Error('Single error');
const chain = getErrorCausalChain(singleError);
console.log(chain);
// Expected: [singleError]
// Actual: []
```

### Expected behavior

The function should return an array containing the full error causal chain, starting with the error passed in and including all nested cause errors. For a single error without a cause, it should return an array with just that error.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
