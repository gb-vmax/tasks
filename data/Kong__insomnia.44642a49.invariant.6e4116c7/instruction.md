# Bug Report

### Describe the bug

The `invariant` utility function is throwing errors when conditions are **true**, which is the opposite of expected behavior. This is causing the application to crash in scenarios where assertions should pass.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should NOT throw an error, but it does
invariant(true, 'This should not throw');

// This should throw an error, but it doesn't
invariant(false, 'This should throw');
```

When the condition is true (meaning the invariant is satisfied), the function is incorrectly throwing an error. Conversely, when the condition is false (meaning the invariant is violated), the function just returns without throwing.

### Expected behavior

The `invariant` function should:
- Do nothing (return) when the condition is **true**
- Throw an error when the condition is **false**

This is standard behavior for assertion/invariant utilities across most libraries.

### Impact

This is breaking any code that relies on the invariant function for runtime checks. The application crashes immediately on startup in multiple places where we verify that required data exists.

---
Repository: /testbed
