# Bug Report

### Describe the bug

The `invariant()` utility function is not throwing errors when it should. When I pass a condition that should fail (evaluates to false), the function just returns instead of throwing an error. This is causing silent failures in my application where invalid states are not being caught.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should throw an error but doesn't
invariant(false, 'This condition failed');
console.log('This line should never execute');

// Another example with a function message
invariant(null, () => 'Value is null');
console.log('Still executing when it should have thrown');
```

### Expected behavior

When the condition is falsy, `invariant()` should throw an error with the provided message. The code after the invariant call should not execute.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
