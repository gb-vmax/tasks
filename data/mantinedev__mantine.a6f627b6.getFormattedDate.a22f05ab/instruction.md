# Bug Report

### Describe the bug

When using a custom `formatter` function with date formatting utilities, the formatter is being called without any arguments. The date object and other formatting options that should be passed to the custom formatter are not being provided, causing the formatter to fail or produce incorrect results.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const customFormatter = (options) => {
  console.log(options); // undefined - expected to receive date and locale info
  return options.date.toLocaleDateString(options.locale);
};

const result = getFormattedDate({
  date: new Date('2024-01-15'),
  locale: 'en-US',
  formatter: customFormatter
});

// Error: Cannot read property 'date' of undefined
```

### Expected behavior

The custom formatter function should receive an object containing the date, locale, and other formatting options as arguments, similar to how the default formatter works. The formatter should be able to access these values to perform custom date formatting.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
