# Bug Report

### Describe the bug

I'm experiencing an issue with hotkey parsing where certain key names aren't being normalized correctly. When using specific key combinations, the hotkey doesn't trigger as expected.

### Reproduction

```js
// This hotkey doesn't work as expected
useHotkeys([
  ['Control+ArrowUp', () => console.log('Arrow up pressed')]
]);

// The key name 'ArrowUp' should be normalized but it's not being matched correctly
```

When I try to use arrow keys or other special keys with the `useHotkeys` hook, the hotkey handler doesn't fire. It seems like the key name normalization is not working properly for keys that have entries in the `keyNameMap`.

### Expected behavior

The hotkey should be recognized and the callback should be triggered when pressing Control+ArrowUp. The key normalization function should properly map special key names to their normalized forms.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120

---
Repository: /testbed
