# Bug Report

### Describe the bug

I'm experiencing an issue with hotkey parsing where special keys defined in the `keyNameMap` are not being recognized correctly. Keys like `esc`, `space`, `enter`, etc. are being treated as their lowercase literal values instead of being mapped to their proper key codes.

### Reproduction

```js
import { useHotkeys } from '@mantine/hooks';

// Try to register a hotkey for the Escape key
useHotkeys([
  ['esc', () => console.log('Escape pressed')],
]);

// Press the Escape key - the handler doesn't fire
// The key is being treated as literal 'esc' instead of being mapped to 'Escape'
```

This affects all special keys that have mappings in the keyNameMap, including:
- `esc` → should map to `Escape`
- `space` → should map to ` `
- `enter` → should map to `Enter`
- Arrow keys (`up`, `down`, `left`, `right`)
- etc.

### Expected behavior

Special key names should be properly mapped to their corresponding key values according to the `keyNameMap`. When I press the Escape key and have registered a hotkey for `'esc'`, the handler should be triggered.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome 120

---
Repository: /testbed
