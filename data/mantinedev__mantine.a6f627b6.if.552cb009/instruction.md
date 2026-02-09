# Bug Report

### Describe the bug

I'm experiencing an issue with form list state clearing functionality. When trying to clear list state, the function doesn't properly validate the input state type, which causes unexpected behavior. 

The state clearing logic appears to be checking for the wrong type - it's checking if the state is a function instead of an object, which means valid object states are being treated incorrectly and cleared when they shouldn't be.

### Reproduction

```js
import { clearListState } from '@mantine/form';

// This should clear list-related fields but doesn't work as expected
const state = {
  'list.0.name': 'error1',
  'list.1.name': 'error2',
  'otherField': 'error3'
};

const result = clearListState('list', state);

// Expected: { otherField: 'error3' }
// Actual: {} (all fields are cleared)
```

Also, when passing `null` or `undefined` as state, the function behaves inconsistently:

```js
// These should return empty object but behavior is unpredictable
clearListState('list', null);
clearListState('list', undefined);
```

### Expected behavior

The function should:
1. Properly validate that the state is an object (not a function)
2. Only clear fields that match the specified list field
3. Preserve non-list fields in the state
4. Handle null/undefined states correctly using strict equality check

### System Info
- @mantine/form version: latest
- Framework: React

---
Repository: /testbed
