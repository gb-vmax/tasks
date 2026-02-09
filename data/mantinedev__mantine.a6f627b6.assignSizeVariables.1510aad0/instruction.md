# Bug Report

### Describe the bug

CSS variables for sizes are being generated with incorrect names and values. The variable names and values appear to be swapped - the size key (like 'xs', 'sm', 'md') is being used as the value, while the actual size value is being used in the variable name.

### Reproduction

```js
import { MantineProvider } from '@mantine/core';

// When using default theme with sizes like:
// sizes = { xs: '10px', sm: '20px', md: '30px' }

// Expected CSS variables:
// --mantine-[name]-xs: 10px
// --mantine-[name]-sm: 20px
// --mantine-[name]-md: 30px

// But actually getting:
// --mantine-[name]-10px: xs
// --mantine-[name]-20px: sm
// --mantine-[name]-30px: md
```

This results in CSS variables that can't be properly referenced in styles since the variable names now contain the pixel values instead of the size keys.

### Expected behavior

CSS variables should be generated with the size key (xs, sm, md, etc.) in the variable name and the actual size value (10px, 20px, 30px, etc.) as the variable's value.

### System Info
- @mantine/core: latest
- Browser: Any

---
Repository: /testbed
