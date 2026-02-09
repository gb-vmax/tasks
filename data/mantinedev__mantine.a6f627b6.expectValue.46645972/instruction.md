# Bug Report

### Describe the bug

I'm experiencing an issue with date input validation where values with leading/trailing whitespace are being incorrectly accepted. When I enter a date with extra spaces, the input appears to accept it without any validation errors, even though the trimmed value should be what's validated against.

### Reproduction

```js
import { DateInput } from '@mantine/dates';

function Demo() {
  return (
    <DateInput
      label="Pick date"
      placeholder="Pick date"
      value={new Date()}
    />
  );
}
```

Steps to reproduce:
1. Render a DateInput component
2. Enter a date value with trailing/leading spaces (e.g., "  01/15/2024  ")
3. The component validates against the non-trimmed value instead of the trimmed one

### Expected behavior

The DateInput should trim whitespace from entered values before validation, so that "  01/15/2024  " is treated the same as "01/15/2024". Currently it seems like the validation is checking against the raw input including spaces, which causes unexpected behavior.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
