# Bug Report

### Describe the bug

The `camelToKebabCase` utility function is producing incorrect output. Instead of converting camelCase strings to kebab-case, it's converting them to something completely different with uppercase letters and dashes in unexpected places.

### Reproduction

```js
import { camelToKebabCase } from '@mantine/core';

// Expected: 'background-color'
// Actual: '-B-A-C-K-G-R-O-U-N-D-C-O-L-O-R'
console.log(camelToKebabCase('backgroundColor'));

// Expected: 'font-size'
// Actual: '-F-O-N-T-S-I-Z-E'
console.log(camelToKebabCase('fontSize'));

// Expected: 'z-index'
// Actual: '-Z-I-N-D-E-X'
console.log(camelToKebabCase('zIndex'));
```

### Expected behavior

The function should convert camelCase strings to kebab-case format:
- `backgroundColor` → `background-color`
- `fontSize` → `font-size`
- `zIndex` → `z-index`

Instead, it's adding dashes before every letter and converting them all to uppercase.

### System Info
- @mantine/core version: latest
- Browser: N/A (utility function)

---
Repository: /testbed
