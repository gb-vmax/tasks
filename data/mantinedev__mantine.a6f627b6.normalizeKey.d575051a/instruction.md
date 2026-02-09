# Bug Report

### Describe the bug

The `useHotkeys` hook is not correctly handling certain key combinations. When using hotkeys with special key names that need normalization, the key matching fails and the hotkey callback doesn't trigger.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+KeyA', () => console.log('Should trigger on Ctrl+A')],
  ]);
  
  return <div>Press Ctrl+A</div>;
}
```

When pressing `Ctrl+A`, the callback doesn't fire. It seems like the key name normalization is not working properly for keys that have the "Key" prefix in their event code.

### Expected behavior

The hotkey callback should trigger when the specified key combination is pressed, regardless of whether the key is specified with or without the "Key" prefix.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
