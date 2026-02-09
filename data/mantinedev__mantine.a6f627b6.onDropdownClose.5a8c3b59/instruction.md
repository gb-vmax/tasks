# Bug Report

### Describe the bug

After a recent update, the Select component crashes when the dropdown closes if no `onDropdownClose` callback is provided. The component is trying to call `onDropdownClose()` even when it's undefined, resulting in a runtime error.

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
1. Create a Select component without providing an `onDropdownClose` prop
2. Open the dropdown
3. Close the dropdown (by clicking outside or selecting an option)
4. Application crashes with "Cannot call undefined" error

### Expected behavior

The Select component should work correctly even when `onDropdownClose` is not provided. The callback should be optional, and the component should only call it if it's defined.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
