# Bug Report

### Describe the bug

When passing `null` to `DateInput`, I'm getting an empty string returned instead of `null`. This is causing issues with my form validation logic that expects `null` for empty date fields.

### Reproduction

```js
import { dateStringParser } from '@mantine/dates';

// This should return null but returns empty string instead
const result = dateStringParser(null);
console.log(result); // Expected: null, Actual: ""
```

### Expected behavior

When `dateStringParser` receives `null` as input, it should return `null` to indicate no date value, not an empty string. This is important for differentiating between "no value selected" and an actual empty string value.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
