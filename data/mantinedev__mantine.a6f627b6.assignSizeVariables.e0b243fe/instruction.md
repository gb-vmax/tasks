# Bug Report

### Describe the bug

CSS variables for component sizes are being generated with incorrect names and values. The variable names are using the actual size value instead of the size key, and the variable values are using the size key instead of the actual value.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

// With size configuration like:
const sizes = {
  xs: '0.875rem',
  sm: '1rem',
  md: '1.125rem',
  lg: '1.25rem',
  xl: '1.5rem'
};

// Expected CSS variables:
// --mantine-component-xs: 0.875rem
// --mantine-component-sm: 1rem
// etc.

// But getting:
// --mantine-component-0.875rem: xs
// --mantine-component-1rem: sm
// etc.
```

### Expected behavior

CSS variables should be generated with the size key (xs, sm, md, etc.) in the variable name and the actual size value (0.875rem, 1rem, etc.) as the variable value.

For example: `--mantine-spacing-md: 1.125rem` instead of `--mantine-spacing-1.125rem: md`

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
