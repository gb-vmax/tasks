# Bug Report

### Describe the bug

The date picker component is showing unexpected behavior when checking if the popover/dropdown is closed. When the popover should not be visible, the component still appears to have a dropdown element present in the DOM.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  return <DateInput />;
}

// When the date picker is closed (not focused/clicked)
// Expected: No dropdown should be visible
// Actual: A dropdown element with data-dates-dropdown-menu attribute is present
```

Steps to reproduce:
1. Render a DateInput component
2. Don't click or focus on it (keep it closed)
3. Check the DOM for dropdown elements
4. The dropdown menu element is still present when it shouldn't be

### Expected behavior

When the date picker popover is closed, there should be no dropdown elements in the DOM. The component should only render the dropdown when the user interacts with the input field.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
