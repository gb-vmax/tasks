# Bug Report

### Describe the bug

The MultiSelect component crashes when the dropdown closes if no `onDropdownClose` callback is provided. The component works fine when the dropdown is opened, but closing it results in an error.

### Reproduction

```jsx
import { MultiSelect } from '@mantine/core';

function Demo() {
  return (
    <MultiSelect
      data={['React', 'Angular', 'Vue']}
      // No onDropdownClose prop provided
    />
  );
}
```

Steps to reproduce:
1. Create a MultiSelect component without providing an `onDropdownClose` prop
2. Click to open the dropdown
3. Click outside or press Escape to close the dropdown
4. The component throws an error

### Expected behavior

The dropdown should close normally even when no `onDropdownClose` callback is provided. The prop should be optional and the component should handle the case where it's undefined.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
