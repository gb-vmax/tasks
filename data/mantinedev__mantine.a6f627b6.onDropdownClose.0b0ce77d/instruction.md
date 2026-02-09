# Bug Report

### Describe the bug

The Select component is throwing an error when the dropdown closes. After closing the dropdown, I'm getting a "Cannot read properties of undefined" error in the console, and the component seems to be breaking.

### Reproduction

```jsx
import { Select } from '@mantine/core';

function Demo() {
  return (
    <Select
      data={['React', 'Angular', 'Vue']}
      placeholder="Pick a framework"
    />
  );
}
```

Steps to reproduce:
1. Click on the Select component to open the dropdown
2. Click outside or press Escape to close the dropdown
3. Error appears in console

The error happens every time the dropdown closes, regardless of whether an option was selected or not.

### Expected behavior

The dropdown should close cleanly without throwing any errors. The component should remain functional after closing.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
