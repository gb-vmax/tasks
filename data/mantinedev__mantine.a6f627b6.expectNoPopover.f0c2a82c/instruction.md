# Bug Report

### Describe the bug

When checking that a date picker popover is not visible, the component is incorrectly reporting that no popover exists even when one is actually present. This seems to be causing validation to pass when it shouldn't.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return <DateInput />;
}

// After closing the popover or when it should not be visible:
// - Expected: No popover dropdown should be in the DOM
// - Actual: The popover dropdown is still present but the check passes incorrectly
```

Steps to reproduce:
1. Render a DateInput component
2. Ensure the popover is closed or should not be visible
3. Check for the presence of popover elements in the DOM
4. The validation incorrectly indicates no popover exists

### Expected behavior

When the popover is closed or not visible, there should be no `[data-dates-dropdown]` elements in the DOM, and the validation should correctly detect when a popover is still present.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
