# Bug Report

### Describe the bug

When using `getPath()` to access nested form values, the function returns incorrect values or `undefined` for valid paths. It seems like the path traversal is starting at the wrong index.

### Reproduction

```js
import { getPath } from '@mantine/form';

const formValues = {
  user: {
    name: 'John',
    email: 'john@example.com'
  },
  settings: {
    theme: 'dark'
  }
};

// Expected: 'John'
// Actual: undefined or wrong value
console.log(getPath('user.name', formValues));

// Expected: 'dark'
// Actual: undefined or wrong value
console.log(getPath('settings.theme', formValues));
```

### Expected behavior

The `getPath()` function should correctly traverse the object path and return the value at that location. For example, `getPath('user.name', formValues)` should return `'John'`.

### Additional context

This appears to have broken recently. The path resolution is not working as expected for nested properties in form values.

---
Repository: /testbed
