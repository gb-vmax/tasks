# Bug Report

### Describe the bug

The TagsInput component crashes when the dropdown closes if no `onDropdownClose` callback is provided. The component seems to be calling the callback even when it's undefined, causing a runtime error.

### Reproduction

```jsx
import { TagsInput } from '@mantine/core';

function App() {
  return (
    <TagsInput
      label="Tags"
      placeholder="Enter tags"
      data={['React', 'Vue', 'Angular']}
    />
  );
}
```

Steps to reproduce:
1. Render a TagsInput without providing an `onDropdownClose` prop
2. Click on the input to open the dropdown
3. Click outside or press Escape to close the dropdown
4. Application crashes with "onDropdownClose is not a function" error

### Expected behavior

The dropdown should close normally without errors when `onDropdownClose` is not provided. The callback should be optional and only called if it's defined.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
