# Bug Report

### Describe the bug
The ColorPicker component is not parsing hex color values correctly. When I pass a hex color string, the resulting color displayed is completely wrong - the RGB channels seem to be shifted or misaligned.

### Reproduction
```js
import { ColorPicker } from '@mantine/core';

// Using a 3-character hex color
<ColorPicker value="#f00" /> // Expected red, but shows wrong color

// Using a 6-character hex color  
<ColorPicker value="#ff0000" /> // Expected red, but shows wrong color
```

The issue appears with both short-form (3 character) and long-form (6 character) hex colors. The color that gets displayed doesn't match what I'm passing in.

### Expected behavior
When passing `#f00` or `#ff0000`, the ColorPicker should display red. Similarly, other hex values like `#0f0` (green) or `#00f` (blue) should display their correct colors.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
