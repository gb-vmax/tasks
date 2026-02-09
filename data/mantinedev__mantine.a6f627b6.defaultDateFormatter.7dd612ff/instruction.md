# Bug Report

### Describe the bug

When using the date picker with `type="range"` and only selecting a start date (without selecting an end date yet), the label separator is missing from the displayed value. The formatted output should show the start date followed by the separator, but currently it only shows the start date without any separator.

### Reproduction

```jsx
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<[Date | null, Date | null]>([new Date(), null]);
  
  return (
    <DatePickerInput
      type="range"
      value={value}
      onChange={setValue}
      labelSeparator=" – "
    />
  );
}
```

When only the start date is selected (end date is `null`), the input displays just the date without the separator. For example, it shows `Jan 1, 2024` instead of `Jan 1, 2024 – `.

### Expected behavior

When a start date is selected in a range picker but the end date is not yet selected, the formatted label should include the separator after the start date to indicate that a range selection is in progress. This provides better visual feedback to the user that they need to select an end date.

Expected: `Jan 1, 2024 – `
Actual: `Jan 1, 2024`

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
