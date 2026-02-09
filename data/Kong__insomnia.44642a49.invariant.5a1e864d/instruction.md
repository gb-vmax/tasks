# Bug Report

### Describe the bug

The `invariant` function is throwing errors when conditions are **true** instead of when they're **false**. This is causing the application to crash in scenarios where it should be running normally.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should NOT throw an error, but it does
invariant(true, 'This should not throw');

// This should throw an error, but it doesn't
invariant(false, 'This should throw');
```

When I call `invariant` with a truthy condition and a message, it immediately throws an error. The function seems to be checking the condition backwards - it throws when the condition is met rather than when it fails.

### Expected behavior

The `invariant` function should:
- Do nothing when the condition is truthy
- Throw an error with the provided message when the condition is falsy

This is the standard behavior for assertion/invariant functions in most libraries.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
