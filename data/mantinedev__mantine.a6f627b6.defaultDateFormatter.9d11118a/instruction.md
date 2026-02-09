# Bug Report

### Describe the bug

I'm experiencing an issue with date formatting in the DatePicker component. When a date is selected, the input field shows an empty string instead of displaying the formatted date. This appears to be affecting the default date picker type.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(new Date());
  
  return (
    <DatePicker
      value={value}
      onChange={setValue}
    />
  );
}
```

When you select a date from the picker, the input field remains empty instead of showing the formatted date value.

### Expected behavior

The input field should display the selected date in the formatted string (e.g., "Jan 15, 2024" or whatever format is specified). Currently it just shows an empty string even though the date value is set correctly.

### Additional context

This seems to have started happening recently. The date value itself is being stored correctly (I can see it in the state), but the visual representation in the input is broken. Range pickers also seem to be affected - they show the separator even when only one date is selected.

---
Repository: /testbed
