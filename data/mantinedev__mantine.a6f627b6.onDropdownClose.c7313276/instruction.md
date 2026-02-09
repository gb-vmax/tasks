# Bug Report

### Describe the bug

The Autocomplete component crashes when `onDropdownClose` prop is not provided. Getting an error when the dropdown closes without explicitly passing an `onDropdownClose` handler.

### Reproduction

```jsx
import { Autocomplete } from '@mantine/core';

function App() {
  return (
    <Autocomplete
      data={['React', 'Angular', 'Vue']}
      // Not providing onDropdownClose prop
    />
  );
}
```

Steps to reproduce:
1. Create an Autocomplete component without the `onDropdownClose` prop
2. Click on the input to open the dropdown
3. Click outside or press Escape to close the dropdown
4. Application crashes with "onDropdownClose is not a function" error

### Expected behavior

The component should work fine without providing the `onDropdownClose` prop since it's optional. The dropdown should close normally without throwing an error.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
