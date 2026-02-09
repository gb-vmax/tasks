# Bug Report

### Describe the bug

When clearing a date selection in a date picker component, the `onChange` callback is now receiving `null` values in the array, which breaks validation logic that expects only valid date strings.

### Reproduction

```js
const [value, setValue] = useState('');

<DatePicker
  value={value}
  onChange={(val) => {
    // Expected: array with date strings only
    // Actual: array can contain null values
    console.log(val); // Shows array with null
    setValue(val);
  }}
  placeholder="test-placeholder"
/>
```

Steps to reproduce:
1. Open the date picker
2. Select a date
3. Click to clear/deselect the date
4. The onChange callback receives an array containing `null` instead of filtering it out

### Expected behavior

The `onChange` callback should only receive arrays containing valid date strings, not `null` values. This was the previous behavior and breaking this causes issues with form validation that expects string values.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
