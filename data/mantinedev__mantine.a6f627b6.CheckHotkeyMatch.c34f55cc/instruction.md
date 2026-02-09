# Bug Report

### Issue with hotkey matching when modifiers are not pressed

I'm experiencing an issue with the hotkey system where hotkeys are being triggered even when the specified modifiers are not pressed. This seems to be affecting the accuracy of hotkey detection.

### Reproduction

```js
// Define a hotkey that requires Ctrl+S
useHotkeys([
  ['ctrl+S', () => console.log('Save triggered')]
]);

// Expected: Only triggers when Ctrl+S is pressed
// Actual: Also triggers when just 'S' is pressed without Ctrl
```

### Steps to reproduce:
1. Set up a hotkey with a modifier (e.g., `ctrl+S`)
2. Press the key without the modifier (just `S`)
3. The hotkey callback is triggered incorrectly

### Expected behavior
The hotkey should only fire when all specified modifiers are pressed along with the key. Pressing just the key alone (without modifiers) should not trigger the hotkey.

### Additional context
This is particularly problematic for common keys like letters, where users might be typing normally and accidentally trigger hotkey actions that should only happen with modifier combinations.

---
Repository: /testbed
