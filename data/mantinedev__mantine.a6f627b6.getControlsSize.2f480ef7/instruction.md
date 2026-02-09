# Bug Report

### Keyboard navigation broken in date picker calendar

I've encountered an issue with keyboard navigation in the date picker component. When trying to navigate through the calendar using arrow keys, the navigation doesn't work as expected - it seems like the controls aren't being mapped correctly.

### Reproduction
```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps to reproduce:
// 1. Open the date picker
// 2. Try to navigate using arrow keys (Up/Down/Left/Right)
// 3. Navigation behaves incorrectly or doesn't respond
```

### Expected behavior
Arrow key navigation should move focus between dates in the calendar grid correctly, respecting the calendar layout structure.

### Additional context
This appears to be related to how the calendar controls are being processed internally. The keyboard navigation was working fine in previous versions but seems to have regressed recently.

---
Repository: /testbed
