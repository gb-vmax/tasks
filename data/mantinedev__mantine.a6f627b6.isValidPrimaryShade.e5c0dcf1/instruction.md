# Bug Report

### Describe the bug

I'm experiencing an issue with `primaryShade` validation in the MantineProvider. When I try to set `primaryShade` to `9`, the theme configuration is being rejected as invalid, even though the documentation states that valid values are integers from 0-9.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        primaryShade: 9  // This throws an error
      }}
    >
      {/* app content */}
    </MantineProvider>
  );
}
```

The error message I get is:
```
[@mantine/core] MantineProvider: Invalid theme.primaryShade, it accepts only 0-9 integers or an object { light: 0-9, dark: 0-9 }
```

### Expected behavior

According to the docs, `primaryShade` should accept values from 0 to 9 (inclusive). Setting it to `9` should be valid and not throw an error.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
