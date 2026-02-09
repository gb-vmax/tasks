# Bug Report

### Describe the bug

The calendar component is not correctly selecting day buttons when querying the DOM. The current selector `table button` matches all buttons within the table element, but it should only match direct children buttons that have proper ARIA labels for accessibility.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return <Calendar />;
}

// When trying to interact with calendar days programmatically:
const container = document.querySelector('.calendar-container');
const dayButtons = container.querySelectorAll('table button');
// This returns incorrect elements including nested buttons without proper ARIA attributes
```

### Expected behavior

The day selection should only target buttons that are direct children of the table element and have `aria-label` attributes, ensuring proper accessibility and avoiding selection of unintended button elements that might be nested within the table structure.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
