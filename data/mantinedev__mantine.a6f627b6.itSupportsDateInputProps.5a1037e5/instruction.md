# Bug Report

### Describe the bug

When using date input components with `allowSingleDateInRange` prop, clicking on a single date is not behaving correctly. The input value is being set to the placeholder text instead of the actual selected date value, and the onChange callback is receiving `null` values instead of the expected date string.

### Reproduction

```jsx
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(null);
  
  return (
    <DatePickerInput
      type="range"
      placeholder="test-placeholder"
      allowSingleDateInRange
      value={value}
      onChange={setValue}
    />
  );
}
```

Steps to reproduce:
1. Render a date input component with `type="range"` and `allowSingleDateInRange` enabled
2. Click on the input to open the calendar
3. Select a single date from the calendar
4. Observe the input value and onChange callback

### Expected behavior

- The input should display the selected date value, not the placeholder text
- The onChange callback should receive an array containing the selected date string, not null values

### Actual behavior

- The input value shows "test-placeholder" after selecting a date
- The onChange callback receives an array containing null instead of the date string

This seems like a regression as single date selection in range mode was working previously.

---
Repository: /testbed
