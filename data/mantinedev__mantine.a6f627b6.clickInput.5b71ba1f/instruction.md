# Bug Report

### Describe the bug

When trying to interact with date inputs in the component, clicking on the input field doesn't work as expected. The click event appears to be targeting the wrong element, causing the date picker popover to not open or the input to not receive focus.

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

When clicking on the date input field, the expected behavior (popover opening or input focusing) doesn't happen. It seems like the click is not being registered on the correct element.

### Expected behavior

Clicking on the date input should:
1. Open the date picker popover
2. Focus the input field
3. Allow the user to interact with the date selection

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
