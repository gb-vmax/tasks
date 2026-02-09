# Bug Report

### Describe the bug

I'm experiencing an issue with the date picker control interactions. When trying to click on calendar controls (like next/previous month buttons), the wrong element is being targeted and the click doesn't work as expected.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  return <DatePicker />;
}

// When trying to interact with calendar controls:
// 1. Render the DatePicker component
// 2. Try to click on the first control button (e.g., previous month)
// 3. The click doesn't register on the button
```

The issue seems to be that when clicking calendar controls by index, the selector is targeting the wrong DOM element. Instead of selecting buttons within the table, it's selecting table elements directly.

### Expected behavior

Clicking on calendar control buttons (like navigation arrows) should properly target the button elements and trigger the expected navigation behavior.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
