# Bug Report

### Describe the bug

The `camelToKebabCase` utility function is not converting camelCase strings to kebab-case correctly. It seems to be dropping characters or producing malformed output.

### Reproduction

```js
import { camelToKebabCase } from '@mantine/core';

// Expected: 'background-color'
// Actual: 'backgroun-olor'
console.log(camelToKebabCase('backgroundColor'));

// Expected: 'font-size'
// Actual: 'fon-ize'
console.log(camelToKebabCase('fontSize'));

// Expected: 'z-index'
// Actual: '-ndex'
console.log(camelToKebabCase('zIndex'));
```

The function appears to be eating characters during the conversion. This is breaking CSS property names when they're being converted from camelCase to kebab-case.

### Expected behavior

The function should properly convert camelCase strings to kebab-case format:
- `backgroundColor` → `background-color`
- `fontSize` → `font-size`
- `zIndex` → `z-index`

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
