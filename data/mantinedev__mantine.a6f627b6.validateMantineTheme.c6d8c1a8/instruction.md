# Bug Report

### Describe the bug

When setting `primaryShade` as an object with both `dark` and `light` properties, the theme validation is not working correctly. If only one of the shade values is invalid (outside the 0-9 range), the validation passes when it should throw an error.

### Reproduction

```js
import { MantineProvider } from '@mantine/core';

// This should throw an error but doesn't
const theme = {
  primaryColor: 'blue',
  primaryShade: {
    light: 5,  // valid
    dark: 15   // invalid - should be 0-9
  }
};

<MantineProvider theme={theme}>
  <App />
</MantineProvider>
```

### Expected behavior

The validation should throw `INVALID_PRIMARY_SHADE_ERROR` when either the `dark` or `light` shade value is outside the valid range (0-9). Currently it only throws an error if BOTH values are invalid.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
