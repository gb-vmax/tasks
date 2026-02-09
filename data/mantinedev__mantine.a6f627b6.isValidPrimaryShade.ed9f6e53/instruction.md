# Bug Report

### Describe the bug

I'm encountering an issue with `MantineProvider` where setting `theme.primaryShade` to `9` is being rejected as invalid, even though the documentation states that valid values are integers from 0-9. The error message says it only accepts 0-9 integers, but shade value `9` throws an error.

### Reproduction

```tsx
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

`primaryShade: 9` should be accepted as a valid value since the error message explicitly states that values 0-9 are valid. All integer values from 0 to 9 (inclusive) should work without errors.

Also noticed that non-integer values like `5.5` seem to be accepted now, which doesn't seem right either based on the error message.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
