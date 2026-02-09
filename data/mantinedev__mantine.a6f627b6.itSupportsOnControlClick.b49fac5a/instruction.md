# Bug Report

### Describe the bug
The `__onControlClick` callback is not receiving the date parameter when clicking on calendar controls. The callback is being invoked but the date argument is undefined/missing.

### Reproduction
```jsx
<DatePicker
  __onControlClick={(event, date) => {
    console.log(date); // Expected: date string, Actual: undefined
  }}
/>
```

When clicking on a date button in the calendar, the `__onControlClick` handler fires but the `date` parameter is not passed to the callback function.

### Expected behavior
The `__onControlClick` callback should receive two parameters:
1. The click event
2. The date value as a string

Currently only the event is being passed, making it impossible to determine which date was clicked.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
