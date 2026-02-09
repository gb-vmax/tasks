# Bug Report

### Describe the bug

When using `HeadlessMantineProvider`, calling `setColorScheme` with an invalid color scheme value causes the function to return early without actually changing the color scheme. The condition check appears to be inverted - it returns `false` when the scheme is valid instead of when it's invalid.

### Reproduction

```tsx
import { HeadlessMantineProvider, useMantineColorScheme } from '@mantine/core';

function App() {
  const { setColorScheme } = useMantineColorScheme();
  
  return (
    <HeadlessMantineProvider>
      <button onClick={() => setColorScheme('dark')}>
        Switch to Dark Mode
      </button>
    </HeadlessMantineProvider>
  );
}
```

When clicking the button:
1. The `setColorScheme('dark')` is called
2. Nothing happens - the color scheme doesn't change
3. The function returns `false` even though 'dark' is a valid scheme

### Expected behavior

The color scheme should change to 'dark' when calling `setColorScheme('dark')`. Valid schemes ('light', 'dark', 'auto') should be accepted and applied, while invalid schemes should be rejected.

Currently it seems like the validation logic is backwards - valid schemes are being rejected and the function returns early without applying any changes.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
