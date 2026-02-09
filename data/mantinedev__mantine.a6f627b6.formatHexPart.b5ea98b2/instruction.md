# Bug Report

### Describe the bug

The ColorPicker component is generating incorrect hex color values. When converting colors to hex format, the output is malformed and doesn't represent valid hex color codes.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try converting any color to hex format
const picker = <ColorPicker format="hex" />;

// Select any color - the hex output will be incorrect
// For example, selecting pure red should give #ff0000
// but instead produces an invalid hex string
```

Or programmatically:

```js
import { hsvaToHex } from '@mantine/core';

// Convert red color to hex
const red = { h: 0, s: 100, v: 100, a: 1 };
const hexColor = hsvaToHex(red);

console.log(hexColor); // Expected: #ff0000, but getting incorrect output
```

### Expected behavior

The ColorPicker should generate valid hex color codes. For example:
- Pure red should be `#ff0000`
- Pure blue should be `#0000ff`
- White should be `#ffffff`

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

This seems to have broken recently - hex colors were working fine before. The converted values don't match standard hex color format anymore.

---
Repository: /testbed
