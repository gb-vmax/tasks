# Bug Report

### Describe the bug

The `dateStringParser` function in `DateInput` is returning `undefined` instead of `null` when handling null/undefined input values. This breaks expected behavior for components that rely on `null` to represent an empty/cleared date state.

### Reproduction

```js
import { dateStringParser } from '@mantine/dates';

// This now returns undefined instead of null
const result = dateStringParser(null);
console.log(result); // Expected: null, Actual: undefined
```

### Expected behavior

When passing `null` to `dateStringParser`, it should return `null` to maintain consistency with the component's API and allow proper handling of cleared/empty date states. Returning `undefined` can cause issues with controlled components that expect `null` as a valid empty state value.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
