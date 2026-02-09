# Bug Report

### Describe the bug

After a recent update, keyboard navigation in date picker components is preventing default browser behavior even when no valid navigation direction is detected. This causes issues with normal text input and other keyboard interactions that should work normally.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

// When using a DatePicker component
<DatePicker />

// Try pressing keys that aren't arrow keys (e.g., Tab, Enter, Space)
// These keys now have their default behavior prevented even though
// they shouldn't be handled by the control navigation logic
```

Steps to reproduce:
1. Open a page with a DatePicker component
2. Focus on a date cell
3. Press a key that isn't an arrow key (like Tab or Enter)
4. Notice that the default browser behavior is blocked

### Expected behavior

Only arrow keys (up, down, left, right) used for navigation should have their default behavior prevented. Other keys should work normally and allow standard browser/form interactions.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox/Safari

---
Repository: /testbed
