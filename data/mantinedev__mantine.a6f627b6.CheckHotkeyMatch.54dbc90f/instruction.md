# Bug Report

### Describe the bug

The hotkey matching logic is not working correctly when the key name contains the event key as a substring. For example, if I register a hotkey for `"ctrl+s"`, it will also match when I press `"ctrl+shift"` or any other key that contains the letter "s".

### Reproduction

```js
import { isHotkeyMatch } from '@mantine/hooks';

// This should only match Ctrl+S
const hotkey = 'ctrl+s';

// Create a mock KeyboardEvent for Ctrl+Shift
const event = new KeyboardEvent('keydown', {
  key: 'Shift',
  ctrlKey: true,
  shiftKey: true
});

// This incorrectly returns true because 'shift'.includes('s') is true
console.log(isHotkeyMatch(hotkey, event)); // Expected: false, Actual: true
```

The issue is that the key matching is using `key.includes(eventKey)` which matches substrings instead of exact keys. So pressing Shift when the hotkey is registered for "s" will trigger a match since "shift" contains "s".

### Expected behavior

The hotkey should only match when the exact key is pressed, not when the key name contains the registered key as a substring. In the example above, `ctrl+s` should only match when the "S" key is pressed with Ctrl, not when Shift or any other key containing "s" is pressed.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome

---
Repository: /testbed
