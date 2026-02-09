# Bug Report

### Describe the bug

When using date input components and checking that no popover is displayed, the validation is incorrectly checking for the presence of a dropdown instead of verifying its absence. This causes tests to pass when a popover is actually visible, which is the opposite of the intended behavior.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return <DateInput />;
}

// When the popover should NOT be visible:
// 1. Render the DateInput component
// 2. Keep the input unfocused/closed
// 3. Check that no popover is displayed

// Expected: No popover should be present
// Actual: The check passes even when a popover IS displayed
```

### Expected behavior

When verifying that no popover is shown, the test helper should confirm that the dropdown element is absent from the DOM. Currently it's checking for the wrong condition - looking for the presence of an element when it should be checking for absence.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
