# Bug Report

### Describe the bug

The CheckIcon component is not rendering properly in the Checkbox component. When the checkbox is in a checked state (not indeterminate), the check mark icon doesn't appear or behaves unexpectedly.

### Reproduction

```jsx
import { Checkbox } from '@mantine/core';

function App() {
  return (
    <Checkbox 
      label="Test checkbox"
      defaultChecked
    />
  );
}
```

When checking the checkbox, the checkmark icon should appear but it seems like props are not being passed correctly to the CheckIcon component.

### Expected behavior

The CheckIcon should receive all necessary props and render the checkmark correctly when the checkbox is in a checked state.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
