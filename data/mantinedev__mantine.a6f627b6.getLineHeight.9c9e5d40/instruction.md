# Bug Report

### Describe the bug

The `getLineHeight` utility function is returning incorrect values. It appears to be using the wrong CSS variable reference, returning font-size values instead of line-height values.

### Reproduction

```js
import { getLineHeight } from '@mantine/core';

// This should return line-height values but returns font-size instead
const lineHeight = getLineHeight('sm');
console.log(lineHeight); // Returns font-size value, not line-height
```

When trying to use `getLineHeight` with any size parameter, the function returns font-size CSS variable values rather than the expected line-height values. This breaks any component or styling that relies on proper line-height calculations.

### Expected behavior

`getLineHeight` should return CSS variable references for `mantine-line-height` values, not `mantine-font-size` values.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
