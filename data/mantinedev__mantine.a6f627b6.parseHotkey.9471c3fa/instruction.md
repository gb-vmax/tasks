# Bug Report

### Describe the bug

When using `useHotkeys` hook with the `+` (plus) key, the hotkey doesn't work as expected. The plus key should be parseable using the `[plus]` syntax, but it seems like the key mapping is incorrect.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+[plus]', () => console.log('Ctrl + Plus pressed')],
  ]);
  
  // Pressing Ctrl + Plus doesn't trigger the callback
  return <div>Try pressing Ctrl + Plus</div>;
}
```

### Expected behavior

When pressing `Ctrl` + `+` (plus key), the hotkey callback should be triggered. The `[plus]` syntax should correctly parse to the `+` character.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120

---
Repository: /testbed
