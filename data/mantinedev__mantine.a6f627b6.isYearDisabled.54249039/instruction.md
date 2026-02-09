# Bug Report

### Describe the bug

I'm experiencing an issue with the YearsList component where all years appear to be disabled when no `minDate` or `maxDate` is provided. This is preventing users from selecting any year in the year picker.

### Reproduction

```jsx
import { YearPickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(null);
  
  return (
    <YearPickerInput
      label="Pick year"
      placeholder="Pick year"
      value={value}
      onChange={setValue}
    />
  );
}
```

When clicking to open the year picker, all years are disabled and cannot be selected. This only happens when neither `minDate` nor `maxDate` props are specified.

### Expected behavior

When no date restrictions are set (no `minDate` or `maxDate`), all years should be selectable. The year picker should allow free selection of any year.

### Additional context

This seems to have started recently. As a workaround, I can set a very wide range using `minDate` and `maxDate`, but this shouldn't be necessary for unrestricted year selection.

---
Repository: /testbed
