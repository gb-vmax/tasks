# Bug Report

### Describe the bug

The `invariant` utility function is not throwing errors when it should. When passing a falsy condition, the function returns early instead of throwing an error, which is the opposite of expected behavior.

### Reproduction

```js
import { invariant } from './utils/invariant';

// This should throw an error but doesn't
invariant(false, 'This condition failed');
console.log('This line should not be reached');

// This also doesn't throw
invariant(null, () => 'Computed error message');
console.log('Still executing...');
```

### Expected behavior

The `invariant` function should throw an error when the condition is falsy. It should only return (do nothing) when the condition is truthy. This is the standard behavior for assertion utilities.

Currently:
- `invariant(false, 'message')` - returns without error ❌
- `invariant(true, 'message')` - throws error ❌

Expected:
- `invariant(false, 'message')` - should throw error
- `invariant(true, 'message')` - should return without error

### System Info
- Package: insomnia
- Affected file: `packages/insomnia/src/utils/invariant.ts`

---
Repository: /testbed
