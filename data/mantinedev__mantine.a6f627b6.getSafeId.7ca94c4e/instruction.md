# Bug Report

### Describe the bug

I'm experiencing an issue with ID generation in Mantine components. When using components that rely on `getSafeId`, the generated IDs are incorrect and contain the error message text instead of the expected UID prefix.

### Reproduction

```js
import { getSafeId } from '@mantine/core';

const generateId = getSafeId('my-component', 'ID is required');

// Calling the function with a value
const id = generateId('input-1');

console.log(id);
// Expected: "my-component-input-1"
// Actual: "ID is required-input-1"
```

This affects any component that uses `getSafeId` internally for generating unique identifiers. The IDs end up being malformed with error message text instead of the component's UID.

### Expected behavior

The generated ID should use the provided `uid` parameter as the prefix, not the `errorMessage` parameter. For example, if `uid` is `'my-component'` and the value is `'input-1'`, the result should be `'my-component-input-1'`.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
