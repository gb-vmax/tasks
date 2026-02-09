# Bug Report

### Describe the bug

I'm experiencing an issue with hotkey detection after a recent update. When I register a hotkey with modifier keys (like Ctrl, Alt, Shift, or Meta), the hotkey never triggers even when I press the correct key combination.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

// None of these hotkeys work anymore
useHotkeys([
  ['ctrl+s', () => console.log('Save')],
  ['alt+k', () => console.log('Alt K')],
  ['shift+d', () => console.log('Shift D')],
  ['meta+enter', () => console.log('Meta Enter')]
]);
```

When I press Ctrl+S or any other combination with modifiers, nothing happens. The callback functions are never called.

### Expected behavior

The hotkey callbacks should fire when the correct key combination is pressed. For example, pressing Ctrl+S should trigger the save callback.

### Additional context

This seems to have started after the latest changes to the hotkey parsing logic. Hotkeys without modifiers (just single keys) still work fine, but any combination involving Ctrl, Alt, Shift, or Meta doesn't trigger anymore.

---
Repository: /testbed
