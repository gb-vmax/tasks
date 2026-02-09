# Bug Report

### Describe the bug

The ColorPicker component is not parsing hex color values correctly. When I pass a hex color string, the resulting color displayed is completely wrong - it seems like the RGB values are being extracted incorrectly from the hex string.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Using 3-character hex notation
<ColorPicker value="#f0a" />
// Expected: pink/magenta color
// Actual: displays wrong color

// Using 6-character hex notation  
<ColorPicker value="#ff0099" />
// Expected: bright pink
// Actual: displays incorrect color
```

The color values seem to be shifted or extracted from wrong positions in the hex string. For example, `#f0a` should expand to `#ff00aa` but it appears to be parsed incorrectly.

### Expected behavior

Hex color strings (both 3-char and 6-char formats) should be parsed correctly and display the expected color in the ColorPicker.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
