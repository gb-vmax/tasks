# Bug Report

### Describe the bug

The ColorPicker component is displaying incorrect colors when parsing shorthand hex color codes (3 characters). The colors appear shifted or completely wrong compared to what they should be.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Using shorthand hex colors
<ColorPicker value="#f00" /> // Should show red, but displays wrong color
<ColorPicker value="#0f0" /> // Should show green, but displays wrong color
<ColorPicker value="#00f" /> // Should show blue, but displays wrong color
```

When I pass a 3-character hex color like `#f00` (red), the picker shows a completely different color. Same issue happens with other shorthand hex values like `#0f0` or `#abc`.

### Expected behavior

Shorthand hex colors should expand correctly:
- `#f00` should be interpreted as `#ff0000` (red)
- `#0f0` should be interpreted as `#00ff00` (green)  
- `#00f` should be interpreted as `#0000ff` (blue)
- `#abc` should be interpreted as `#aabbcc`

The ColorPicker should display the correct color for these shorthand values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
