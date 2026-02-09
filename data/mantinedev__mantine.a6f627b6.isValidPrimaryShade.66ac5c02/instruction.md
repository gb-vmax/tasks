# Bug Report

### Describe the bug
I'm having an issue with setting `theme.primaryShade` to 9 in MantineProvider. The theme validation is rejecting shade value 9 even though the documentation states that primaryShade accepts integers from 0-9.

### Reproduction
```jsx
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

When I try to use `primaryShade: 9`, I get the following error:
```
[@mantine/core] MantineProvider: Invalid theme.primaryShade, it accepts only 0-9 integers or an object { light: 0-9, dark: 0-9 }
```

### Expected behavior
According to the error message itself, primaryShade should accept values from 0-9, so setting it to 9 should be valid and not throw an error.

### System Info
- @mantine/core version: latest
- React version: 18.x

This seems like it might be a validation bug since the error message says 0-9 is acceptable but 9 is being rejected.

---
Repository: /testbed
