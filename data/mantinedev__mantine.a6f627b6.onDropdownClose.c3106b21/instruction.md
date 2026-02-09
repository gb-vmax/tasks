# Bug Report

### Describe the bug

The Autocomplete component crashes when the dropdown closes if no `onDropdownClose` prop is provided. This happens because the code is trying to call `onDropdownClose()` without checking if it's defined first.

### Reproduction

```jsx
import { Autocomplete } from '@mantine/core';

function App() {
  return (
    <Autocomplete
      data={['React', 'Angular', 'Vue']}
      // Not passing onDropdownClose prop
    />
  );
}
```

**Steps to reproduce:**
1. Create an Autocomplete component without passing the `onDropdownClose` prop
2. Click on the input to open the dropdown
3. Click outside or press Escape to close the dropdown
4. The app crashes with an error

### Expected behavior

The Autocomplete should work fine even when `onDropdownClose` is not provided. It's an optional callback and the component should handle the case where it's undefined.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
