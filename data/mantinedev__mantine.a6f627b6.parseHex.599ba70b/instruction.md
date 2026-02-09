# Bug Report

### Describe the bug

The ColorPicker component is not parsing hex color values correctly. When I try to use 3-character or 6-character hex colors, the resulting colors are completely wrong.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try using a 3-character hex color like #f00 (red)
<ColorPicker value="#f00" />
// The displayed color is incorrect

// Also happens with 6-character hex colors like #ff0000
<ColorPicker value="#ff0000" />
// Again, wrong color is displayed
```

When I pass `#f00` (which should be red), the color picker shows a different color entirely. Same issue happens with full 6-digit hex codes like `#ff0000`.

### Expected behavior

- `#f00` should be parsed as red (RGB: 255, 0, 0)
- `#ff0000` should also be parsed as red
- The ColorPicker should display the correct color based on the hex input

### System Info
- @mantine/core version: latest
- Browser: Firefox 121

---
Repository: /testbed
