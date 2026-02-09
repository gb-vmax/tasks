# Bug Report

### Describe the bug

When clicking on date picker controls, the component doesn't maintain the correct input value. After clicking certain dates in the calendar, the input field gets cleared or shows unexpected values instead of preserving the previously selected date.

### Reproduction

```jsx
const DatePickerComponent = () => {
  const [value, setValue] = useState(new Date());
  
  return (
    <DateInput
      value={value}
      onChange={setValue}
      placeholder="test-placeholder"
    />
  );
};
```

Steps to reproduce:
1. Open the date picker by clicking the input
2. Select a date from the calendar (the input shows the selected date)
3. Open the date picker again
4. Click on another date in the calendar
5. The input value doesn't update correctly or gets reset

### Expected behavior

The input should maintain its value after selecting dates from the calendar. When clicking different dates, the input should update to show the newly selected date without losing the previous value unexpectedly.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
