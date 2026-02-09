# Bug Report

### Describe the bug

The `invariant` utility function is not throwing errors when it should. When passing a falsy condition, the function returns early instead of throwing an error, which is the opposite of what an invariant check should do.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should throw an error but doesn't
invariant(false, 'This condition is false');
console.log('This line should never be reached');

// Another example - validating required data
const data = null;
invariant(data !== null, 'Data is required');
// Execution continues even though data is null
processData(data); // This will cause issues later
```

### Expected behavior

The `invariant` function should throw an error when the condition is falsy. It should only return (do nothing) when the condition is truthy. This is standard behavior for assertion/invariant utilities.

Expected:
- `invariant(true, 'message')` → no error, continues execution
- `invariant(false, 'message')` → throws error with the message

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
