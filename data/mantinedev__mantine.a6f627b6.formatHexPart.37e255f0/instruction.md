# Bug Report

### Describe the bug

The ColorPicker component is generating incorrect hex color codes. When converting colors to hex format, the output is completely wrong and produces invalid color strings.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try to use ColorPicker and convert to hex
const picker = <ColorPicker format="hex" />;

// Or try converting colors programmatically
// Any color conversion to hex format will produce wrong results
// For example, RGB(255, 0, 0) should give #ff0000 but produces something else
```

### Expected behavior

The ColorPicker should generate valid hex color codes. For example:
- Pure red (RGB 255, 0, 0) should output `#ff0000`
- Pure white (RGB 255, 255, 255) should output `#ffffff`
- Black (RGB 0, 0, 0) should output `#000000`

Instead, the hex values are completely incorrect and don't represent the selected colors properly.

### System Info
- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
