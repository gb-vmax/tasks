# Bug Report

### Describe the bug

The `useHotkeys` hook is not triggering callbacks when keys are pressed. The hotkey combinations are registered but nothing happens when I actually press the key combination.

### Reproduction

```tsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+K', () => console.log('Ctrl+K pressed')],
    ['mod+S', () => console.log('Save triggered')],
  ]);

  return <div>Press Ctrl+K or Cmd+S (Mac)</div>;
}
```

When pressing the key combinations, the callbacks are not being executed. I can see the component renders fine but the hotkeys just don't work.

### Expected behavior

The callback functions should be executed when the corresponding key combinations are pressed down.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
