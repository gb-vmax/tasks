# Bug Report

### Describe the bug

When clearing list state in forms, the function is not properly resetting the state object. Instead of clearing the state, it appears to be returning the original state unchanged, which prevents proper form cleanup.

### Reproduction

```js
import { clearListState } from '@mantine/form';

const state = {
  'list.0': { error: 'some error' },
  'list.1': { error: 'another error' },
  'otherField': { value: 'test' }
};

const result = clearListState('list', state);

// Expected: state should be cleared/reset to empty object
// Actual: state is returned as-is without being cleared
console.log(result); // Still contains all the original properties
```

### Expected behavior

The `clearListState` function should properly clear/reset the state object when called. Currently it seems to just return the state without any modifications, which means form errors and values persist when they should be removed.

### System Info
- @mantine/form version: latest
- Framework: React

---
Repository: /testbed
