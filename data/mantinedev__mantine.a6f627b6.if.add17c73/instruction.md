# Bug Report

### Describe the bug

I'm experiencing an issue with the `useHotkeys` hook where hotkeys with the `mod` modifier are not working correctly on Mac. When I define a hotkey using `mod+key` (which should map to `cmd+key` on Mac and `ctrl+key` on Windows/Linux), the hotkey doesn't trigger on Mac when pressing `cmd+key`.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['mod+s', () => console.log('Save triggered')],
  ]);

  return <div>Press cmd+s on Mac (or ctrl+s on Windows)</div>;
}
```

Steps to reproduce:
1. Set up a component with a `mod+key` hotkey
2. On macOS, press `cmd+key`
3. The hotkey callback doesn't fire

The same code works fine on Windows/Linux with `ctrl+key`, but fails on Mac with `cmd+key`.

### Expected behavior

The `mod` modifier should work consistently across platforms - mapping to `cmd` on Mac and `ctrl` on Windows/Linux. Pressing `cmd+s` on Mac should trigger the hotkey callback just like `ctrl+s` does on Windows.

### System Info
- @mantine/hooks version: latest
- OS: macOS
- Browser: Chrome 120

---
Repository: /testbed
