# Bug Report

### Describe the bug

I'm experiencing an issue with date input components where clicking on the input field doesn't open the date picker popover as expected. The click event seems to be targeting the wrong element.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return (
    <DateInput
      label="Pick a date"
      placeholder="Click to open"
    />
  );
}
```

When I click directly on the input field (the actual text input area), nothing happens. The date picker popover should open but it doesn't respond to clicks.

### Expected behavior

Clicking on the date input field should open the date picker popover, allowing the user to select a date from the calendar view.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- Browser: Chrome/Firefox

This seems to have started happening recently. The input field is visible and styled correctly, but the click interaction is broken.

---
Repository: /testbed
