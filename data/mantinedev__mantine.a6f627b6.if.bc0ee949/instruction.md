# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with `DateInput` when passing an empty string as the value. The component doesn't handle empty strings correctly - it seems to be treating them differently than `null` values.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

// This doesn't work as expected
<DateInput value="" />

// Expected: empty string should be handled gracefully
// Actual: component behavior is inconsistent
```

When I pass an empty string to the `DateInput` component, it's not being processed correctly by the date parser. The parser should distinguish between `null` and empty string values, but currently it only checks for `null`.

### Expected behavior

The `dateStringParser` function should handle empty strings appropriately:
- When `dateString` is `null`, it should return `null`
- When `dateString` is an empty string `''`, it should return `''`
- When `dateString` is a valid date string, it should parse and return the date

Currently, empty strings are being passed through to `new Date('')` which creates an invalid date instead of being handled separately.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
