# Bug Report

### Keyboard navigation broken in date picker components

I'm experiencing issues with keyboard navigation in the date picker. When using arrow keys to navigate between dates, the navigation seems to stop working or skip dates unexpectedly.

### Reproduction
```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps:
// 1. Open the date picker calendar
// 2. Focus on a date cell
// 3. Try navigating with arrow keys (up/down/left/right)
// 4. Navigation doesn't work as expected - some dates are skipped or unreachable
```

### Expected behavior
Arrow key navigation should move smoothly between all available dates in the calendar. Each arrow key press should move to the adjacent date cell in the corresponding direction.

### Additional context
This seems to have started recently. The keyboard controls were working fine before, but now the navigation feels broken - it's like some cells are being excluded from the navigation grid.

---
Repository: /testbed
