# Bug Report

### Describe the bug

I'm encountering an issue with hotkey parsing where only the first non-modifier key is being captured. When trying to define hotkeys with multiple regular keys (not modifiers), the parser seems to ignore all but one of them.

### Reproduction

```js
// Trying to register a hotkey with multiple keys
useHotkeys([
  ['ctrl+a+b', () => console.log('pressed')]
]);
```

When I press `ctrl+a+b`, the hotkey doesn't trigger as expected. It seems like the parser is only looking at one of the non-modifier keys instead of handling multiple keys properly.

### Expected behavior

The hotkey parser should handle combinations that include multiple non-modifier keys. If I specify `ctrl+a+b`, it should capture both `a` and `b` as part of the key combination.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120

---
Repository: /testbed
