# Bug Report

### Describe the bug

When configuring `MantineProvider` with a theme that has an invalid `primaryShade` object, the validation is not working correctly. Specifically, if I provide a valid `light` shade but an invalid `dark` shade, the theme is accepted without throwing an error.

### Reproduction

```js
import { MantineProvider } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  primaryShade: {
    light: 6,  // valid
    dark: 15   // invalid (should be 0-9)
  }
};

// This should throw an error but doesn't
<MantineProvider theme={theme}>
  <App />
</MantineProvider>
```

### Expected behavior

The provider should throw an `INVALID_PRIMARY_SHADE_ERROR` when either the `light` or `dark` shade value is outside the valid range (0-9). Currently it seems like the validation only fails if both values are invalid.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
