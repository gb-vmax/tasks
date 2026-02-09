# Bug Report

### Describe the bug

When using a custom `formatter` function with date components, the formatter is not receiving the correct date-related parameters. Instead, it appears to be called with an empty object `{}`, which means the formatter cannot access the date value or any other necessary formatting options.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const customFormatter = (input) => {
  console.log(input); // Expected: { date, locale, format, ... }
                      // Actual: {}
  return input.date ? input.date.toLocaleDateString() : '';
};

const result = getFormattedDate({
  formatter: customFormatter,
  date: new Date('2024-01-15'),
  locale: 'en-US',
  format: 'MM/DD/YYYY'
});

// The formatter receives an empty object instead of the date parameters
// This causes the formatter to fail or return incorrect results
```

### Expected behavior

The custom formatter function should receive all the date-related parameters (date, locale, format, etc.) that were passed to `getFormattedDate`, not an empty object. This allows the formatter to properly format the date based on the provided inputs.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
