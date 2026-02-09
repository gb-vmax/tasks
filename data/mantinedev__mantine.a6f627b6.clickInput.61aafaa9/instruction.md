# Bug Report

### Describe the bug

The date input component is not responding to clicks properly. When I try to click on the date input field, nothing happens - the popover doesn't open and the input doesn't receive focus.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function Demo() {
  return (
    <DateInput
      label="Pick date"
      placeholder="Pick date"
    />
  );
}
```

Steps to reproduce:
1. Render a DateInput component
2. Click on the input field
3. Expected: The date picker popover should open
4. Actual: Nothing happens, the input doesn't respond to clicks

This seems to have started happening recently. The input field is rendered correctly but clicking on it has no effect.

### Expected behavior

Clicking on the date input should open the date picker popover and allow the user to select a date.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
