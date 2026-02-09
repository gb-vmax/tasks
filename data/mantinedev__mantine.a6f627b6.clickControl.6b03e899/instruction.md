# Bug Report

### Describe the bug

The `clickControl` helper function in date input tests is not working correctly. When trying to click on calendar controls (like next/previous month buttons), the function appears to be selecting the wrong element. Instead of clicking the button at the specified index, it seems to be targeting table elements.

### Reproduction

```js
// Using the clickControl helper to click a calendar button
const container = render(<DateInput />);
clickControl(container, 0); // Expected to click first button, but clicks wrong element
```

When using `clickControl(container, index)` to interact with calendar controls:
1. The function should click on calendar buttons (next/prev month, year selection, etc.)
2. Instead, it appears to be selecting table elements rather than the buttons within them
3. This causes tests to fail when trying to navigate the calendar

### Expected behavior

The `clickControl` function should click on the button at the specified index within the calendar table, allowing proper interaction with calendar controls for navigation and date selection.

### System Info
- Package: @mantine/dates
- Test helpers affected: date-input-test-helpers.ts

---
Repository: /testbed
