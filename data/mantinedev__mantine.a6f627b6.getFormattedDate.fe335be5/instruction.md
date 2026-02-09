# Bug Report

### Describe the bug

I'm experiencing an issue with date formatting in the `@mantine/dates` package. When I pass custom formatter options like `date`, `locale`, and `format` to components that use date formatting internally, the dates are not being formatted correctly. It seems like the formatter is receiving the wrong arguments.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const result = getFormattedDate({
  date: new Date('2024-01-15'),
  locale: 'en-US',
  format: 'MMMM DD, YYYY'
});

console.log(result); // Expected: "January 15, 2024"
// Actual: undefined or error
```

The same issue occurs when using DatePicker or other date components with custom formatting options - the dates either don't display or show unexpected output.

### Expected behavior

The date should be formatted according to the provided options (date, locale, format). When using a custom formatter function, it should receive all the necessary parameters to properly format the date.

### System Info
- @mantine/dates version: latest
- @mantine/core version: 7.x
- Browser: Chrome 120

---
Repository: /testbed
