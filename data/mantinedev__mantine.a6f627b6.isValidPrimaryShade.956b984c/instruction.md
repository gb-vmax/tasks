# Bug Report

### Describe the bug

I'm experiencing an issue with `primaryShade` validation in `MantineProvider`. When I try to set `primaryShade` to `9`, the theme throws an error saying it's invalid, even though the documentation states that valid values are integers from 0-9.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        primaryShade: 9
      }}
    >
      {/* App content */}
    </MantineProvider>
  );
}
```

This throws an error: `[@mantine/core] MantineProvider: Invalid theme.primaryShade, it accepts only 0-9 integers or an object { light: 0-9, dark: 0-9 }`

### Expected behavior

`primaryShade: 9` should be accepted as a valid value since the valid range is documented as 0-9 (inclusive). Currently, only values 0-8 seem to work.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
