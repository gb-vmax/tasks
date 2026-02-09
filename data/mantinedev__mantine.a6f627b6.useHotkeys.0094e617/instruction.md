# Bug Report

### Describe the bug

The `useHotkeys` hook is firing handlers even when the hotkey combination doesn't match. It seems like hotkeys are being triggered regardless of whether the key combination is correct or not.

### Reproduction

```tsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+K', () => console.log('Ctrl+K pressed')],
  ]);

  return <div>Press any key and check console</div>;
}
```

When testing this:
1. Press any random key (like 'A' without ctrl)
2. The handler fires even though the hotkey combination doesn't match
3. Expected: handler should only fire when ctrl+K is pressed

### Expected behavior

Hotkey handlers should only execute when the exact key combination is matched. Pressing keys that don't match the hotkey pattern should not trigger the handler.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
