# Bug Report

### Describe the bug

CSS variables are being rendered with extra spaces between them when using `MantineProvider`. The generated CSS string contains unnecessary whitespace that wasn't present before, which can cause issues with CSS parsing and increase bundle size.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

// When CSS variables are converted to string
const variables = {
  '--color-primary': '#000',
  '--color-secondary': '#fff',
  '--spacing': '16px'
};

// The output now includes spaces between variable declarations
// Expected: '--color-primary: #000;--color-secondary: #fff;--spacing: 16px;'
// Actual: '--color-primary: #000; --color-secondary: #fff; --spacing: 16px;'
```

### Expected behavior

CSS variable declarations should be concatenated without spaces between them, just like before. The output should be a compact string without unnecessary whitespace.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
