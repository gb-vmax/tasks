# Bug Report

### Describe the bug

The keyboard shortcut display is showing incorrect key combinations. It seems like the function is returning early and not respecting platform-specific modifier key ordering anymore.

### Reproduction

When trying to display keyboard shortcuts, the output doesn't follow the expected platform conventions:

```js
// On macOS, shortcuts should follow the order: Ctrl, Alt, Shift, Meta
// But currently getting wrong order or incomplete combinations

const keyComb = {
  ctrl: true,
  shift: true,
  meta: true,
  keyCode: 'S'
};

const display = constructKeyCombinationDisplay(keyComb, true);
// Expected on Mac: ⌃⌥⇧⌘+S (or similar platform-specific format)
// Getting: incorrect or incomplete output
```

### Expected behavior

The function should:
1. Display modifier keys in the correct platform-specific order (Control, Option, Shift, Command on macOS)
2. Handle different platforms (Mac vs Windows/Linux) appropriately
3. Properly join keys with '+' when `mustUsePlus` is true

### System Info
- Insomnia version: latest
- OS: macOS / Windows / Linux (affects all platforms)

This appears to have broken after a recent change. The keyboard shortcuts in the UI are now displaying incorrectly or not at all.

---
Repository: /testbed
