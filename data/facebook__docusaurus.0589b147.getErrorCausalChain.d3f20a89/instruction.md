# Bug Report

### Describe the bug

The error causal chain is being returned in the wrong order. When an error has a `cause` property, the chain should show the root cause first, but instead it's showing the most recent error first.

### Reproduction

```js
const rootError = new Error('Root cause');
const middleError = new Error('Middle error', { cause: rootError });
const topError = new Error('Top error', { cause: middleError });

const chain = getErrorCausalChain(topError);
console.log(chain.map(e => e.message));
// Current output: ['Top error', 'Middle error', 'Root cause']
// Expected output: ['Root cause', 'Middle error', 'Top error']
```

### Expected behavior

The causal chain should be ordered from the root cause to the final error, not the other way around. This makes it easier to trace the original source of the problem.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
