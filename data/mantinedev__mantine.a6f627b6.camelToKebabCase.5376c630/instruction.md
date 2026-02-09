# Bug Report

### Describe the bug

The `camelToKebabCase` utility function is not converting camelCase strings to kebab-case correctly. When converting strings with uppercase letters, the hyphens are missing from the output.

### Reproduction

```js
import { camelToKebabCase } from '@mantine/core';

// Expected: 'background-color'
// Actual: 'backgroundcolor'
console.log(camelToKebabCase('backgroundColor'));

// Expected: 'font-size'
// Actual: 'fontsize'
console.log(camelToKebabCase('fontSize'));

// Expected: 'border-top-width'
// Actual: 'bordertopwidth'
console.log(camelToKebabCase('borderTopWidth'));
```

### Expected behavior

The function should insert hyphens before uppercase letters and convert them to lowercase. For example:
- `backgroundColor` → `background-color`
- `fontSize` → `font-size`
- `borderTopWidth` → `border-top-width`

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is affecting CSS variable names and style prop conversions in my application. Any help would be appreciated!

---
Repository: /testbed
