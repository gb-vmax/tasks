# Bug Report

### Describe the bug

I'm experiencing an issue with ID generation in Mantine components. When using components that generate IDs based on a value parameter, the generated IDs are not unique as expected. Instead of incorporating the provided value into the ID, it appears to be duplicating the UID portion.

### Reproduction

```tsx
import { getSafeId } from '@mantine/core';

const generateId = getSafeId('input', 'Error message');

// Expecting: 'input-1', 'input-2', etc.
const id1 = generateId('1');
const id2 = generateId('2');

console.log(id1); // Getting: 'input-input' instead of 'input-1'
console.log(id2); // Getting: 'input-input' instead of 'input-2'
```

This causes issues when multiple form fields or components need unique IDs, as they all end up with the same ID value. This breaks accessibility features and can cause conflicts in the DOM.

### Expected behavior

The function should generate unique IDs by combining the UID with the provided value parameter. For example:
- `generateId('1')` should return `'input-1'`
- `generateId('field')` should return `'input-field'`

Instead, it's returning the same ID regardless of the value passed in.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
