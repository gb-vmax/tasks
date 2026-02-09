# Bug Report

### Describe the bug

When using `DateInput` with `allowDeselect` prop enabled, clicking on an already selected date doesn't properly deselect it. The date remains selected instead of being cleared to `null`.

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
1. Render a DateInput component with `allowDeselect` prop set to true
2. Select a date (it becomes highlighted)
3. Click on the same selected date again
4. Expected: the date should be deselected and value should become `null`
5. Actual: the date remains selected

### Expected behavior

When `allowDeselect` is enabled and a user clicks on an already selected date, the value should be set to `null` and the date should no longer appear as selected in the calendar.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
