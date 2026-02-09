# Bug Report

### Describe the bug

When using `MultiSelect` with a custom `onDropdownClose` callback, the application crashes with an error if the prop is not provided. The component should handle the case where `onDropdownClose` is optional.

### Reproduction

```jsx
import { MultiSelect } from '@mantine/core';

function App() {
  return (
    <MultiSelect
      data={['React', 'Angular', 'Vue']}
      label="Select frameworks"
      placeholder="Pick values"
      // Not providing onDropdownClose prop
    />
  );
}
```

### Steps to reproduce:
1. Create a MultiSelect component without passing the `onDropdownClose` prop
2. Open the dropdown
3. Close the dropdown (by clicking outside or pressing Escape)
4. Application crashes

### Expected behavior

The component should work correctly even when `onDropdownClose` is not provided, as it's an optional callback prop.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
