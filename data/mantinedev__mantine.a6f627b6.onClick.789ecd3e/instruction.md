# Bug Report

### Describe the bug

When using `DateInput` with `allowDeselect` enabled, clicking on an already selected date doesn't deselect it as expected. Instead, the date remains selected and the input field doesn't clear.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(new Date());

  return (
    <DateInput
      value={value}
      onChange={setValue}
      allowDeselect
    />
  );
}
```

Steps to reproduce:
1. Create a DateInput component with `allowDeselect` prop set to true
2. Select a date from the calendar
3. Click on the same date again
4. The date should deselect and clear the input, but it doesn't

### Expected behavior

When clicking on an already selected date with `allowDeselect` enabled, the date should be deselected (set to null) and the input field should clear. Currently, the date remains selected.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
