# Bug Report

### Describe the bug

The `onDayKeydown` handler is not being triggered when pressing the Space key on calendar day cells. It only seems to work with the Enter key, which is inconsistent with expected keyboard navigation behavior for date pickers.

### Reproduction

```jsx
<DatePicker
  __onDayKeydown={(payload) => {
    console.log('Key pressed on day:', payload);
  }}
/>
```

Steps to reproduce:
1. Render a date picker component with the `__onDayKeydown` prop
2. Focus on a day cell in the calendar table
3. Press the Space key
4. The handler doesn't fire

However, if you press Enter instead, it works as expected.

### Expected behavior

Both Space and Enter keys should trigger the `__onDayKeydown` handler when pressed on a calendar day cell. Space is a common key for selecting items in accessible UI components, so it should be supported alongside Enter.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
