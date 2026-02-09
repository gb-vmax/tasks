# Bug Report

### Describe the bug

When using the YearsList component with `minDate` set, the minimum year itself is being disabled and cannot be selected. The year picker should allow selecting the minimum year, but it's currently treating it as if it's before the minimum date.

### Reproduction

```jsx
import { YearPickerInput } from '@mantine/dates';

function Demo() {
  return (
    <YearPickerInput
      label="Select year"
      minDate={new Date(2020, 0, 1)}
    />
  );
}
```

When rendered, the year 2020 appears as disabled even though it's set as the minimum date. I should be able to select 2020, but only years 2021 and onwards are selectable.

### Expected behavior

The minimum year (2020 in the example) should be selectable. Only years before the minimum date should be disabled.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
