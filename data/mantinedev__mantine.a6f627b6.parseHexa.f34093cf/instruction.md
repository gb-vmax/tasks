# Bug Report

### Describe the bug

When using the ColorPicker component with hexadecimal color values that include alpha/opacity channels (hexa format), the opacity is not being parsed correctly. Colors with alpha channels are displaying with incorrect transparency values.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Using 4-digit hex with alpha (e.g., #RGBA)
<ColorPicker value="#f00f" /> // Should be red with full opacity
// Displays with incorrect alpha value

// Using 8-digit hex with alpha (e.g., #RRGGBBAA)
<ColorPicker value="#ff0000ff" /> // Should be red with full opacity  
// Displays with incorrect alpha value
```

The issue affects both short-form (4-digit) and long-form (8-digit) hexa color formats. When specifying colors with alpha channels, the transparency is not being calculated properly.

### Expected behavior

The ColorPicker should correctly parse and display colors with alpha channels:
- `#f00f` should render as red with full opacity (f = 255)
- `#ff0000ff` should render as red with full opacity (ff = 255)
- Other alpha values should be proportionally correct

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
