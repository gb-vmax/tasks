# Bug Report

### Describe the bug

The ColorPicker component is not parsing hexadecimal colors with alpha channel (hexa format) correctly. When using 8-digit hex colors like `#RRGGBBAA`, the alpha/opacity value is being read incorrectly, resulting in wrong transparency values.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try using an 8-digit hex color with alpha
const color = '#ff0000ff'; // Red with full opacity (FF = 255 = 1.0)

// The parsed alpha value will be incorrect
// Expected: alpha = 1.0
// Actual: alpha value is wrong due to only reading one hex digit instead of two
```

Similarly, for 4-digit hex colors (short format with alpha):

```js
const shortColor = '#f00f'; // Red with full opacity
// The color parsing is also affected
```

### Expected behavior

- 8-digit hex colors like `#RRGGBBAA` should correctly parse the last two digits as the alpha channel
- 4-digit hex colors like `#RGBA` should correctly parse all color components including alpha
- The alpha value should be properly converted from the hex range (00-FF) to decimal (0.0-1.0)

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
