# Bug Report

### Describe the bug

The `px()` utility function is returning incorrect values when converting CSS units. I'm seeing two main issues:

1. When passing strings with `calc()` or `var()` CSS functions, the function returns `NaN` instead of the original string
2. When converting `rem` units to pixels, the conversion factor seems wrong - getting 10px per rem instead of the standard 16px

### Reproduction

```js
import { px } from '@mantine/core';

// Issue 1: calc/var functions return NaN
console.log(px('calc(100% - 20px)'));
// Expected: 'calc(100% - 20px)'
// Actual: NaN

console.log(px('var(--my-spacing)'));
// Expected: 'var(--my-spacing)'
// Actual: NaN

// Issue 2: rem conversion is incorrect
console.log(px('2rem'));
// Expected: 32 (2 * 16)
// Actual: 20 (2 * 10)
```

### Expected behavior

- CSS calc() and var() expressions should be returned as-is without conversion
- rem units should convert to pixels using the standard 16px base (1rem = 16px)

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
