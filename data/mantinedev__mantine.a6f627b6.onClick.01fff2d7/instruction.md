# Bug Report

### Describe the bug

When using `DateInput` with `allowDeselect` prop enabled, clicking on an already selected date doesn't deselect it as expected. Instead, it seems to behave incorrectly - the date remains selected when it should be cleared.

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
1. Create a DateInput with `allowDeselect` enabled
2. Select a date
3. Click on the same date again
4. Expected: date should be deselected (value becomes null)
5. Actual: date remains selected

This is causing issues in forms where users need to be able to clear date selections. The `allowDeselect` prop doesn't seem to work properly.

### Expected behavior

When `allowDeselect` is true and a user clicks on an already selected date, the date should be deselected and the value should become `null`.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
