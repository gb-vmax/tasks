# Bug Report

### Describe the bug

The ColorPicker component is not correctly parsing hex color values. When I pass a hex color string, the resulting color displayed is completely wrong - the green and blue channels seem to be off.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try parsing a simple hex color
const color = '#ff5733';

<ColorPicker value={color} />
```

When using hex colors like `#ff5733` (which should be a reddish-orange), the picker displays a different color. The issue seems to affect both 3-character shorthand hex codes (like `#f53`) and full 6-character hex codes.

### Expected behavior

The ColorPicker should correctly parse and display hex color values. For example:
- `#ff5733` should display as reddish-orange
- `#f53` should display the same color as `#ff5533`

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
