# Bug Report

### Describe the bug

The Autocomplete component crashes when the dropdown closes if the `onDropdownClose` prop is not provided. The component is calling `onDropdownClose()` without checking if it exists first.

### Reproduction

```jsx
import { Autocomplete } from '@mantine/core';

function MyComponent() {
  return (
    <Autocomplete
      data={['React', 'Angular', 'Vue']}
      // Note: no onDropdownClose prop provided
    />
  );
}
```

Steps to reproduce:
1. Create an Autocomplete component without the `onDropdownClose` prop
2. Open the dropdown by focusing the input
3. Close the dropdown (click outside or press Escape)
4. Application crashes with "onDropdownClose is not a function" error

### Expected behavior

The Autocomplete should work correctly even when `onDropdownClose` is not provided, since it's an optional prop. The component should only call the callback if it's defined.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
