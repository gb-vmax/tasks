# Bug Report

### Describe the bug

The `dateStringParser` function is returning unexpected values for `null` and empty string inputs. When passing `null`, it now returns an empty string `''` instead of `null`, and when passing an empty string `''`, it returns `undefined` instead of handling it consistently.

### Reproduction

```js
import { dateStringParser } from '@mantine/dates';

// This now returns '' instead of null
const result1 = dateStringParser(null);
console.log(result1); // Expected: null, Got: ''

// This now returns undefined
const result2 = dateStringParser('');
console.log(result2); // Expected: consistent behavior with null case
```

### Expected behavior

The function should return `null` when passed `null` as input, maintaining consistency with the previous behavior. The handling of empty strings should also be predictable and consistent with the overall API design.

### System Info
- @mantine/dates version: latest
- TypeScript version: 5.x

This is causing issues in forms where we need to distinguish between "no value selected" (null) and other states. The return type seems inconsistent now.

---
Repository: /testbed
