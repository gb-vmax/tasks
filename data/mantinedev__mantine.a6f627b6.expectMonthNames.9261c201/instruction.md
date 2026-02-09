# Bug Report

### Describe the bug

When using month picker components, the component seems to be selecting more buttons than expected. I'm getting unexpected button elements included in the month selection that shouldn't be there.

### Reproduction

```jsx
// Using any month picker component with the months list
<MonthPicker />
```

When rendering a month picker, if there are any additional buttons in the component (like navigation buttons or other controls), they are being incorrectly included when trying to select only the month buttons.

### Expected behavior

Only the month name buttons from the table should be selected, not other buttons that might exist in the component (navigation buttons, year selectors, etc.). The selector should be specific enough to target only the month buttons within the calendar table.

### System Info
- Mantine version: latest
- Browser: All browsers affected

---
Repository: /testbed
