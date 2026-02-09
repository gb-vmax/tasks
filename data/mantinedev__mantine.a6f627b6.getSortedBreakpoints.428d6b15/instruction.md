# Bug Report

### Describe the bug

I'm experiencing an issue with breakpoint ordering in responsive components. When using multiple breakpoints, they seem to be applied in the wrong order, causing unexpected layout behavior at different screen sizes.

### Reproduction

```js
import { useBreakpoints } from '@mantine/core';

// Define breakpoints with different values
const breakpoints = {
  base: 0,
  sm: 576,
  md: 768,
  lg: 992,
  xl: 1200
};

// When these are sorted, the order is incorrect
// Smaller breakpoints are being prioritized over larger ones
// or vice versa, leading to wrong styles being applied
```

When I resize my browser window, the styles for larger breakpoints are being applied at smaller screen sizes, or the breakpoint logic is completely reversed from what I expect.

### Expected behavior

Breakpoints should be sorted in ascending order by their pixel values so that media queries are applied correctly. The smallest breakpoint should have the lowest priority and the largest should have the highest priority (or vice versa depending on the use case).

### System Info
- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
