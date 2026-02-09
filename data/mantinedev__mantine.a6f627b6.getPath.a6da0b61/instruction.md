# Bug Report

### Describe the bug

I'm experiencing an issue with form path resolution when accessing nested form values. It seems like the `getPath` function isn't correctly retrieving values from nested paths in certain scenarios.

### Reproduction

```js
import { getPath } from '@mantine/form';

const formValues = {
  user: {
    name: 'John',
    address: {
      city: 'New York'
    }
  }
};

// This returns undefined instead of the expected value
const result = getPath('user.name', formValues);
console.log(result); // Expected: 'John', Actual: undefined

// Nested paths also fail
const nestedResult = getPath('user.address.city', formValues);
console.log(nestedResult); // Expected: 'New York', Actual: undefined
```

### Expected behavior

The `getPath` function should correctly traverse the object path and return the value at the specified location. For `'user.name'`, it should return `'John'`, and for `'user.address.city'`, it should return `'New York'`.

### Additional context

This seems to have broken recently. The path resolution was working fine before, but now it's returning `undefined` for paths that should resolve to actual values. It looks like the function might be skipping the first segment of the path or something similar.

---
Repository: /testbed
