# Bug Report

### Describe the bug

The `DateInput` component is not properly validating dates against `minDate` and `maxDate` constraints. When I set a `maxDate`, dates that should be valid are being rejected, and dates that should be invalid are being accepted. The same issue occurs with `minDate` - the validation logic appears to be inverted.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

function Demo() {
  const today = new Date();
  const maxDate = new Date(2024, 11, 31); // December 31, 2024
  const minDate = new Date(2024, 0, 1);   // January 1, 2024

  return (
    <DateInput
      label="Select date"
      minDate={minDate}
      maxDate={maxDate}
      defaultValue={today}
    />
  );
}
```

When testing this:
1. Dates within the valid range (between Jan 1, 2024 and Dec 31, 2024) are being marked as invalid
2. Dates outside this range are being accepted as valid
3. The behavior is completely reversed from what's expected

Also noticed that passing `null` as a date value is now treated differently than before - it's no longer being caught by the validation.

### Expected behavior

- Dates before `minDate` should be invalid
- Dates after `maxDate` should be invalid  
- Dates between `minDate` and `maxDate` should be valid
- `null` date values should be handled consistently

### System Info
- @mantine/dates version: latest
- @mantine/core version: 7.x

---
Repository: /testbed
