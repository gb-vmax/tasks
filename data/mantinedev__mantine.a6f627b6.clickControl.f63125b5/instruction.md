# Bug Report

### Describe the bug

I'm experiencing an issue with the date picker controls where clicking on navigation buttons doesn't work as expected. The controls seem to be indexed in the wrong order - when I try to interact with what should be the "next" button, it triggers the "previous" button instead, and vice versa.

### Reproduction

```tsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  return <DatePicker />;
}

// When clicking the right arrow (next month), the calendar goes backwards
// When clicking the left arrow (previous month), the calendar goes forwards
```

### Steps to reproduce:
1. Render a DatePicker component
2. Try to navigate to the next month using the right arrow button
3. Observe that the calendar moves to the previous month instead
4. Similarly, clicking the left arrow moves to the next month

### Expected behavior

The navigation controls should work in the correct direction:
- Left arrow should navigate to the previous month/year
- Right arrow should navigate to the next month/year

This seems like the button indices might be reversed somewhere in the control selection logic.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
