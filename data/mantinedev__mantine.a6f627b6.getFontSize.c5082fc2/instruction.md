# Bug Report

### Describe the bug

The `getFontSize` utility function is returning incorrect CSS variable names. When trying to use font size values, the generated CSS variable names don't match the expected format, causing styles to not be applied correctly.

### Reproduction

```js
import { getFontSize } from '@mantine/core';

// This should return 'var(--mantine-font-size-md)'
const fontSize = getFontSize('md');
console.log(fontSize); // Actually returns 'var(--mantine-size-font-md)'
```

### Expected behavior

The function should return CSS variables with the correct naming convention: `--mantine-font-size-{value}` instead of `--mantine-size-font-{value}`.

This is breaking font size theming as the CSS variables don't match what's defined in the theme configuration.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
