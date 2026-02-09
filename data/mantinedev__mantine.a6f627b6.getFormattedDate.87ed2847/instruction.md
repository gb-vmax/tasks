# Bug Report

### Describe the bug

I'm having an issue with the date formatting utility in `@mantine/dates`. When I try to format a date using `getFormattedDate`, I'm getting errors about the formatter function not working correctly.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const formatted = getFormattedDate({
  date: new Date(),
  locale: 'en',
  format: 'MM/DD/YYYY'
});

// This throws an error or returns unexpected results
console.log(formatted);
```

### Expected behavior

The function should return a properly formatted date string based on the provided date, locale, and format options. It should work the same way as it did in previous versions.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
