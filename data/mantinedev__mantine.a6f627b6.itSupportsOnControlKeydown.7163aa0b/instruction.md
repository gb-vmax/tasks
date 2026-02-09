# Bug Report

### Describe the bug

The `onControlKeyDown` handler is not being triggered when pressing Enter on date picker input fields. The keyboard event seems to be ignored when interacting with the input elements in the calendar control.

### Reproduction

```jsx
<DatePicker
  onControlKeyDown={(payload) => {
    console.log('Key pressed:', payload);
  }}
/>
```

Steps to reproduce:
1. Render a date picker component with `onControlKeyDown` prop
2. Focus on the input field inside the calendar table
3. Press the Enter key
4. The callback is not invoked

### Expected behavior

The `onControlKeyDown` callback should fire when pressing Enter on the input field, providing the row index, cell index, and date information in the payload.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
