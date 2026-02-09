# Bug Report

### Describe the bug

I'm experiencing an issue with responsive breakpoints where they seem to be applied in the wrong order. The breakpoints appear to be sorted incorrectly, causing styles intended for larger screens to apply on smaller screens and vice versa.

### Reproduction

```js
import { getSortedBreakpoints } from '@mantine/core';

const breakpoints = {
  xs: '36em',
  sm: '48em',
  md: '62em',
  lg: '75em',
  xl: '88em'
};

const values = ['sm', 'md', 'lg'];
const sorted = getSortedBreakpoints(values, breakpoints);

console.log(sorted);
// The breakpoints are returned in reverse order
// Larger breakpoints appear first instead of last
```

When using responsive props or media queries, the styles don't cascade properly because the breakpoint order is inverted.

### Expected behavior

Breakpoints should be sorted from smallest to largest (xs → sm → md → lg → xl) so that media queries and responsive styles apply correctly with proper CSS specificity.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: macOS

---
Repository: /testbed
