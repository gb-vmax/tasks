# Bug Report

### Describe the bug

ColorPicker is not parsing short hex color codes (3-character format) correctly. When using 3-character hex colors like `#fff` or `#f00`, the resulting color appears much darker than expected.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Using 3-character hex color
<ColorPicker value="#fff" />
// Expected: white color
// Actual: displays a very dark/black color

<ColorPicker value="#f00" />
// Expected: bright red
// Actual: displays a dark red/almost black
```

### Expected behavior

Short hex color codes should be expanded correctly. For example:
- `#fff` should be interpreted as `#ffffff` (white)
- `#f00` should be interpreted as `#ff0000` (red)
- `#abc` should be interpreted as `#aabbcc`

Currently the colors appear much darker than they should be, suggesting the hex values aren't being doubled as they should be for 3-character format.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
