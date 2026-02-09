# Bug Report

### Describe the bug

I'm experiencing an issue with responsive breakpoints where the ordering seems reversed and one breakpoint value is missing from the output. When I define multiple breakpoints for a component, the behavior is not what I expect.

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

const values = ['xs', 'sm', 'md', 'lg'];
const result = getSortedBreakpoints(values, breakpoints);

console.log(result);
// Expected: breakpoints sorted from smallest to largest, all 4 values present
// Actual: breakpoints appear in reverse order and only 3 values are returned
```

### Expected behavior

The function should return all provided breakpoints sorted from smallest to largest (ascending order by pixel value). If I pass 4 breakpoint keys, I should get 4 breakpoints back in the result.

### System Info

- @mantine/core version: latest
- React version: 18.x

This is affecting responsive layouts where components need to adapt based on screen size. The reversed order and missing breakpoint is causing incorrect rendering at different viewport widths.

---
Repository: /testbed
