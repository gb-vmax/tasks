# Bug Report

### Describe the bug

The date input component is not opening the popover correctly when clicked. After clicking on the input field, the calendar/date picker popover doesn't appear as expected.

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
3. The popover should open but doesn't appear

### Expected behavior

When clicking on the date input field, the calendar popover should open and allow the user to select a date. The click should target the input element with the `data-dates-input` attribute and trigger the popover to display.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
