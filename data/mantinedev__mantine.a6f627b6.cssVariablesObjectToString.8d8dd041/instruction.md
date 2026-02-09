# Bug Report

### CSS variables rendering issue with undefined/null values

I'm experiencing an issue where CSS variables are being rendered incorrectly when they have undefined or null values. This is causing invalid CSS to be injected into the page.

### Reproduction
```tsx
import { MantineProvider } from '@mantine/core';

// When passing CSS variables with undefined/null values
const cssVariables = {
  '--my-color': 'red',
  '--my-size': undefined,
  '--my-spacing': null
};

// The generated CSS string includes entries like:
// "--my-size: undefined;"
// "--my-spacing: null;"
```

### Expected behavior
CSS variables with undefined or null values should be filtered out and not included in the generated CSS string. The output should only contain valid CSS variable declarations.

### Current behavior
The CSS output includes invalid declarations like `--my-size: undefined;` which breaks styling and causes console warnings about invalid CSS.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

This seems to have started happening recently. Would appreciate any help on this!

---
Repository: /testbed
