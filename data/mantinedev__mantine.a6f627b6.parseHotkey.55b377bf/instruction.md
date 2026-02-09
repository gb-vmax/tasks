# Bug Report

### Describe the bug

I'm experiencing an issue with the `useHotkeys` hook where hotkey combinations are not being recognized correctly. When I try to register a hotkey like `ctrl+S` or `shift+A`, the key detection seems to be broken and the callback doesn't fire as expected.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+S', () => console.log('Save triggered')],
    ['shift+A', () => console.log('Action triggered')],
  ]);

  return <div>Press ctrl+S or shift+A</div>;
}
```

When pressing `ctrl+S` or `shift+A`, nothing happens. The callbacks are never executed.

Also tried with the plus sign hotkey:
```js
useHotkeys([
  ['mod+[plus]', () => console.log('Zoom in')],
]);
```

This also doesn't work - pressing the plus key with modifier doesn't trigger the callback.

### Expected behavior

The hotkey callbacks should be triggered when the correct key combinations are pressed. Both regular key combinations (like `ctrl+S`) and special keys (like `[plus]`) should work properly.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
