# Bug Report

### Describe the bug

When checking if a date picker popover is closed, the validation is not working correctly. It seems like the helper function is checking for the wrong data attribute, causing false positives when the popover should be hidden.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return <DateInput />;
}

// When clicking outside the date input to close the popover
// The expectNoPopover check passes even though it should verify the popover is actually closed
```

Steps to reproduce:
1. Render a DateInput component
2. Click to open the date picker popover
3. Click outside to close it
4. The popover appears to be closed visually but the validation helper doesn't properly detect this state

### Expected behavior

The `expectNoPopover` helper should correctly verify that the date picker dropdown/popover is not present in the DOM when it's closed. Currently it seems to be checking for a different element that's always present.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
