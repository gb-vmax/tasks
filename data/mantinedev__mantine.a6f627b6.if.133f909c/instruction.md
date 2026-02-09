# Bug Report

### Describe the bug

Getting a runtime error when calling `getSeriesLabels` with `undefined` series data. The function is supposed to return an empty object when series is not provided, but instead it's returning `undefined` which causes issues downstream when the code tries to access properties on the result.

### Reproduction

```js
import { getSeriesLabels } from '@mantine/charts';

// This should return {} but returns undefined instead
const labels = getSeriesLabels(undefined);

// Later code that expects an object fails
console.log(Object.keys(labels)); // TypeError: Cannot convert undefined or null to object
```

### Expected behavior

When `series` is `undefined` or `null`, the function should return an empty object `{}` so that consuming code can safely iterate over the result or access properties without additional null checks.

### System Info

- @mantine/charts version: latest
- Node version: 18.x

---
Repository: /testbed
