# Bug Report

### Describe the bug
When using `DateInput` with `allowDeselect` enabled, clicking on an already selected date doesn't deselect it. The date remains selected instead of being cleared.

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
1. Create a DateInput with `allowDeselect` prop
2. Select a date
3. Click on the same date again
4. The date should be deselected (value becomes null), but it stays selected

### Expected behavior
When clicking on an already selected date with `allowDeselect` enabled, the date should be deselected and the value should become `null`.

---
Repository: /testbed
