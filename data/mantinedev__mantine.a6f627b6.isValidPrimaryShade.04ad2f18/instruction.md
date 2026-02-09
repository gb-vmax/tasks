# Bug Report

### Describe the bug

I'm experiencing an issue with the `primaryShade` validation in MantineProvider. It seems like valid shade values are being rejected, and some invalid values are being accepted.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

// This should work but throws an error
<MantineProvider theme={{ primaryShade: 9 }}>
  <App />
</MantineProvider>

// Also this valid configuration is rejected
<MantineProvider theme={{ primaryShade: { light: 9, dark: 9 } }}>
  <App />
</MantineProvider>
```

When I try to use `primaryShade: 9`, I get the error:
```
[@mantine/core] MantineProvider: Invalid theme.primaryShade, it accepts only 0-9 integers or an object { light: 0-9, dark: 0-9 }
```

But according to the documentation, shade values should accept integers from 0 to 9 inclusive. The value 9 should be valid.

### Expected behavior

- `primaryShade` values from 0 to 9 (inclusive) should be accepted as valid
- Negative values should be rejected
- Non-integer values should be rejected

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
