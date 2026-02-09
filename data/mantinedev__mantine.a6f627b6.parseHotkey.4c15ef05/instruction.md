# Bug Report

### Describe the bug

The hotkey parser is not correctly handling the `[plus]` key when it's used as a modifier key. When defining a hotkey like `ctrl+shift+[plus]`, the parser seems to treat `[plus]` as a reserved modifier key instead of recognizing it as the actual key to be pressed.

### Reproduction

```js
import { parseHotkey } from '@mantine/hooks';

// This doesn't work as expected
const hotkey = parseHotkey('ctrl+shift+[plus]');
console.log(hotkey);
// Expected: { ctrl: true, shift: true, key: '+', ... }
// Actual: { ctrl: true, shift: true, key: undefined, ... }
```

The issue is that when `[plus]` appears in the hotkey string, it's being included in the reserved keys list before we try to find the free key, so `freeKey` ends up being `undefined`.

### Expected behavior

The parser should correctly identify `[plus]` as the target key, not as a modifier. The resulting hotkey object should have `key: '+'` with the appropriate modifiers set.

### System Info
- @mantine/hooks version: latest
- Browser: Any

---
Repository: /testbed
