# Bug Report

### Describe the bug

The `useHotkeys` hook is not triggering the callback function when keyboard shortcuts are pressed. The hotkeys appear to be completely unresponsive - nothing happens when I press the key combinations.

### Reproduction

```jsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+K', () => console.log('Ctrl+K pressed')],
    ['mod+S', () => console.log('Save triggered')],
  ]);

  return <div>Press Ctrl+K or Cmd/Ctrl+S</div>;
}
```

When pressing the keyboard shortcuts, the callbacks are never executed. The console.log statements don't appear at all.

### Expected behavior

The callback functions should be executed immediately when the corresponding keyboard shortcuts are pressed down.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
