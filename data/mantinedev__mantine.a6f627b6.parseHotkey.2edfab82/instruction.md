# Bug Report

### Describe the bug

When using `useHotkeys` with the `mod` modifier (e.g., `mod+S`), the hotkey doesn't work as expected. The `mod` key is supposed to map to `Cmd` on macOS and `Ctrl` on other platforms, but it seems like the modifier is not being recognized properly.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['mod+S', () => console.log('Save triggered')],
  ]);

  return <div>Press Cmd+S (Mac) or Ctrl+S (Windows/Linux) to save</div>;
}
```

When pressing `Cmd+S` on Mac or `Ctrl+S` on Windows, nothing happens. The callback is not triggered.

### Expected behavior

The `mod` modifier should be recognized and the hotkey callback should fire when the appropriate key combination is pressed.

### Additional context

This seems to have broken recently. The `mod` modifier was working fine in previous versions. Other modifiers like `ctrl`, `alt`, and `shift` still work correctly when used directly.

---
Repository: /testbed
