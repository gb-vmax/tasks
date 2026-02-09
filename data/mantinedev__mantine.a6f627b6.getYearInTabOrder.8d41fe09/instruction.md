# Bug Report

### Describe the bug

The YearsList component is not correctly handling keyboard navigation. When trying to tab through the year picker, no years are receiving focus. It seems like the tab order calculation is filtering out the wrong years - it's keeping disabled years instead of enabled ones.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function Demo() {
  return (
    <YearPicker 
      minDate={new Date(2020, 0, 1)}
      maxDate={new Date(2030, 11, 31)}
    />
  );
}
```

Steps to reproduce:
1. Render a YearPicker component with min/max date constraints
2. Try to use keyboard navigation (Tab key) to navigate through the years
3. Notice that no years can be focused via keyboard

### Expected behavior

Should be able to tab through enabled years in the picker. The currently selected year (or current year if none selected) should receive focus first, followed by other enabled years.

### Additional context

This appears to affect keyboard accessibility for the year picker component. Mouse clicks still work, but keyboard-only users cannot navigate the year selection.

---
Repository: /testbed
