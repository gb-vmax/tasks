# Bug Report

### Describe the bug

Custom date formatters are not being used when provided to `getFormattedDate`. The function appears to always use the default formatter instead of the custom one passed in the `formatter` parameter.

### Reproduction

```js
import { getFormattedDate } from '@mantine/dates';

const customFormatter = (input) => {
  return 'Custom: ' + input.date.toISOString();
};

const result = getFormattedDate({
  date: new Date('2024-01-15'),
  formatter: customFormatter,
  locale: 'en'
});

console.log(result);
// Expected: "Custom: 2024-01-15T00:00:00.000Z"
// Actual: Uses default formatter output instead
```

### Expected behavior

When a custom `formatter` function is provided, it should be used to format the date instead of the default formatter. The custom formatter should take precedence over the built-in formatting logic.

### System Info

- @mantine/dates version: latest
- Node version: 18.x

---
Repository: /testbed
