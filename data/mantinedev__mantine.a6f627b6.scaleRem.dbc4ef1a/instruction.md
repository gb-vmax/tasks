# Bug Report

### Describe the bug

I'm encountering an issue with the `rem()` utility function where values containing `0rem` anywhere in the string are being incorrectly treated as zero. For example, `10rem` or `20rem` are being converted to `0rem` instead of being properly scaled.

### Reproduction

```js
import { rem } from '@mantine/core';

// This returns '0rem' instead of the expected scaled value
const result = rem('10rem');
console.log(result); // Expected: 'calc(10rem * var(--mantine-scale))', Got: '0rem'

// Same issue with any value containing '0rem' substring
const result2 = rem('20rem');
console.log(result2); // Expected: 'calc(20rem * var(--mantine-scale))', Got: '0rem'
```

### Expected behavior

The `rem()` function should only return `'0rem'` when the input is exactly `'0rem'`, not when the input string merely contains the substring `'0rem'`. Values like `'10rem'`, `'20rem'`, etc. should be properly converted to their calc expressions.

Additionally, there seems to be an issue with the scaling direction - values are being divided by the scale factor instead of multiplied, which produces inverted scaling behavior.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
