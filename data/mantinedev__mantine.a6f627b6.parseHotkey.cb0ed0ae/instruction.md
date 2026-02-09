# Bug Report

### Describe the bug

I'm experiencing an issue with the `useHotkeys` hook where the special `[plus]` key notation is not being parsed correctly. When I try to use `[plus]` in a hotkey combination, it seems to be handled incorrectly and the hotkey doesn't trigger as expected.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+[plus]', () => console.log('Should trigger on Ctrl+Plus')],
  ]);
  
  return <div>Press Ctrl+Plus</div>;
}
```

When pressing `Ctrl` + `+` (plus key), the callback doesn't fire. It seems like the `[plus]` notation isn't being converted to the actual `+` character properly.

### Expected behavior

The hotkey should recognize `[plus]` as the plus key and trigger the callback when the combination is pressed. The `[plus]` escape notation exists specifically to handle the plus character since it's used as a delimiter in hotkey strings.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
