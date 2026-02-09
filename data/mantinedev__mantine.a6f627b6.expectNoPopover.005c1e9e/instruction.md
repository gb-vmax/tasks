# Bug Report

### Describe the bug

I'm experiencing an issue with date picker components where the popover/dropdown is not being detected correctly when it should be closed. The component seems to think a popover exists even when it shouldn't be visible.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  return <DatePicker />;
}

// When checking if the popover is closed:
// Expected: No popover should be present
// Actual: The check fails and indicates a popover exists
```

The issue appears when trying to verify that a date picker dropdown is properly closed. The validation logic seems to be incorrectly identifying the presence of dropdown elements.

### Expected behavior

When the date picker is closed, there should be no dropdown/popover elements in the DOM. The component should correctly identify when the popover is not present.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
