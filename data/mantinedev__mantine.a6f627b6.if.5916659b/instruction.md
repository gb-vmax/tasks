# Bug Report

### Describe the bug

The `getSeriesLabels` function is returning `null` instead of an empty object when the series parameter is `undefined`. This causes a type error when trying to access properties on the returned value, since the function signature indicates it should return a `ChartSeriesLabels` object.

### Reproduction

```ts
import { getSeriesLabels } from '@mantine/charts';

const result = getSeriesLabels(undefined);
console.log(result); // Expected: {}, Actual: null

// This will throw an error
Object.keys(result); // TypeError: Cannot convert undefined or null to object
```

### Expected behavior

When `series` is `undefined`, the function should return an empty object `{}` to maintain consistency with the return type `ChartSeriesLabels` (which is `Record<string, string | undefined>`). This allows consumers to safely iterate or access properties without additional null checks.

### System Info

- @mantine/charts version: latest
- TypeScript version: 5.x

---
Repository: /testbed
