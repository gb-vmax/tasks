# Bug Report

### Describe the bug

I'm experiencing an issue with the `use-hotkeys` hook where certain key combinations are not being recognized properly. Specifically, hotkeys that use special keys like `ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`, `PageUp`, `PageDown`, etc. are failing to trigger their associated handlers.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ArrowUp', () => console.log('Arrow up pressed')],
    ['PageDown', () => console.log('Page down pressed')],
    ['Home', () => console.log('Home pressed')],
  ]);

  return <div>Press ArrowUp, PageDown, or Home keys</div>;
}
```

When pressing these keys, nothing happens. The handlers are not being called even though the keys are being pressed correctly.

### Expected behavior

The hotkey handlers should be triggered when the specified keys are pressed. Keys like `ArrowUp`, `PageDown`, `Home`, `End`, etc. should work the same way as regular letter keys.

### System Info
- @mantine/hooks version: latest
- Browser: Firefox 121
- OS: macOS

---
Repository: /testbed
