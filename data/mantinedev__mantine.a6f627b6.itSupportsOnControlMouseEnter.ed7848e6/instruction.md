# Bug Report

### Describe the bug

The `__onControlMouseEnter` callback is receiving the wrong argument. When hovering over calendar controls, the callback is being passed the event object instead of the date value that should be provided.

### Reproduction

```tsx
<DatePicker
  __onControlMouseEnter={(event, date) => {
    console.log('Date:', date);
    // Expected: date should be a string representing the date
    // Actual: date is undefined, event contains the date instead
  }}
/>
```

When hovering over a calendar date button, the first parameter contains the date string but should contain the mouse event, and the second parameter is undefined but should contain the date.

### Expected behavior

The `__onControlMouseEnter` callback should receive the mouse event as the first argument and the date value as the second argument, matching the function signature `(event: any, date: any) => void`.

### System Info
- @mantine/dates latest version

---
Repository: /testbed
