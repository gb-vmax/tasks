# Bug Report

### Describe the bug

When using the Select component with the `onDropdownClose` callback, the application crashes with an error when the callback prop is not provided. The component tries to call `onDropdownClose()` without checking if it's defined first.

### Reproduction

```jsx
import { Select } from '@mantine/core';

function MyComponent() {
  return (
    <Select
      data={['Option 1', 'Option 2', 'Option 3']}
      // No onDropdownClose prop provided
    />
  );
}
```

Steps to reproduce:
1. Create a Select component without passing the `onDropdownClose` prop
2. Open the dropdown
3. Close the dropdown (click outside or press Escape)
4. Application crashes with "Cannot read property of undefined" or similar error

### Expected behavior

The Select component should work correctly even when the `onDropdownClose` callback is not provided. Optional callbacks should be checked before being invoked.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
