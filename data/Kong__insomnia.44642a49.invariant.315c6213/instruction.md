# Bug Report

### Describe the bug

The `invariant()` utility function is not throwing errors when it should. When a condition fails (evaluates to falsy), the function returns silently instead of throwing an error with the provided message.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should throw an error but doesn't
invariant(false, 'This condition failed');
console.log('Still executing...'); // This line executes when it shouldn't

// Another example with a function message
invariant(null, () => 'Value is null');
console.log('Also still executing...'); // This also executes
```

### Expected behavior

When the condition is falsy, `invariant()` should throw an error and stop execution. The error should contain the message provided (either as a string or from the function).

For example:
```js
invariant(false, 'This should fail');
// Should throw: Error: This should fail
```

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
