# Bug Report

### Describe the bug

When interacting with date input controls in the popover, clicking on certain date controls is not working as expected. Specifically, clicking on disabled or unavailable dates seems to be allowing selection when it shouldn't.

### Reproduction

```jsx
// Create a date input component with some disabled dates
const MyDatePicker = () => {
  const [value, setValue] = useState(null);
  
  return (
    <DateInput
      value={value}
      onChange={setValue}
      excludeDate={(date) => date.getDay() === 0} // Disable Sundays
    />
  );
};

// Steps to reproduce:
// 1. Open the date picker popover
// 2. Click on a disabled date (e.g., a Sunday)
// 3. The date gets selected even though it should be disabled
```

### Expected behavior

Clicking on disabled dates should not trigger a selection. The `onChange` handler should not be called with `null` values or disabled dates. The input value should remain unchanged when clicking on unavailable date controls.

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox
- React version: 18.x

---
Repository: /testbed
