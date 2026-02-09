# Bug Report

### Describe the bug

The `dateStringParser` function is returning `undefined` instead of `null` when passed a `null` value. This breaks the expected behavior and type contracts in the DateInput component.

### Reproduction

```js
import { dateStringParser } from '@mantine/dates';

// This now returns undefined instead of null
const result = dateStringParser(null);
console.log(result); // Expected: null, Actual: undefined
```

### Expected behavior

When `dateStringParser` receives `null` as input, it should return `null` to maintain consistency with the `DateStringValue | null` return type. The function should handle `null` explicitly and return `null`, not `undefined`.

### System Info

- @mantine/dates version: latest
- Node version: 18.x

---
Repository: /testbed
