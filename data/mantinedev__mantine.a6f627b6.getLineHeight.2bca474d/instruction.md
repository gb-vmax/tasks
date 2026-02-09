# Bug Report

### Describe the bug

The `getLineHeight` utility function is returning incorrect values. Instead of retrieving line-height CSS variables, it appears to be fetching height-related values, which is causing layout issues in components that rely on proper line-height calculations.

### Reproduction

```tsx
import { getLineHeight } from '@mantine/core';

// This should return a line-height value like '1.5' or 'calc(...)'
const lineHeight = getLineHeight('md');

console.log(lineHeight);
// Expected: CSS variable for mantine-line-height-md
// Actual: Returns something related to mantine-height instead
```

When using components that depend on `getLineHeight`, text spacing and typography are rendered incorrectly because the function is not retrieving the correct CSS variable values.

### Expected behavior

`getLineHeight` should return values from `--mantine-line-height-*` CSS variables, not height-related variables. This affects any component that uses line-height for text rendering and spacing calculations.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
