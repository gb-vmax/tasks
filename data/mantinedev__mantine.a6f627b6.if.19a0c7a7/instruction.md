# Bug Report

### Describe the bug

Getting a `TypeError` when passing `undefined` to `getParsedComboboxData`. The function is trying to call `.map()` on an undefined value, which causes the application to crash.

### Reproduction

```js
import { getParsedComboboxData } from '@mantine/core';

// This throws an error
const result = getParsedComboboxData(undefined);
// TypeError: Cannot read property 'map' of undefined

// Also fails with null
const result2 = getParsedComboboxData(null);
```

### Expected behavior

When passing `undefined` or `null` as the data parameter, the function should return an empty array `[]` instead of throwing an error. This would be consistent with defensive programming practices and prevent crashes when the data hasn't loaded yet or is unavailable.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
