# Bug Report

### Describe the bug

I'm experiencing an issue with date formatting in the `@mantine/dates` package. When I pass a custom formatter function or use the default formatter, the date is not being formatted correctly. It seems like the formatter is receiving an unexpected object structure instead of the individual date parameters.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const date = new Date('2024-01-15');
const locale = 'en-US';

// Using default formatter
const formatted = getFormattedDate({
  date,
  locale,
  format: 'MMMM DD, YYYY'
});

console.log(formatted); // Expected: "January 15, 2024"
// Actual: formatter doesn't work as expected
```

When using a custom formatter:

```js
const customFormatter = (params) => {
  console.log(params); // Shows wrapped object instead of expected properties
  return params.date.toLocaleDateString();
};

const result = getFormattedDate({
  date: new Date(),
  locale: 'en-US',
  formatter: customFormatter
});
```

### Expected behavior

The formatter function should receive the date parameters directly (date, locale, format, etc.) as individual properties, not wrapped in an additional object layer. The date should be formatted correctly according to the provided format string or custom formatter logic.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
