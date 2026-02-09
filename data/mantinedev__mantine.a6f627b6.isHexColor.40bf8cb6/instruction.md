# Bug Report

### Describe the bug

The `toRgba` function is not accepting valid 3-character hex color codes (shorthand notation). When I try to use colors like `#fff` or `#000`, they're being rejected as invalid, but 6-character hex codes like `#ffffff` work fine.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This should work but doesn't
const white = toRgba('#fff');
const black = toRgba('#000');
const red = toRgba('#f00');

// Only 6-character hex codes work
const whiteExpanded = toRgba('#ffffff'); // This works
```

### Expected behavior

Both shorthand (3-character) and full (6-character) hex color codes should be accepted as valid input. CSS supports both formats, so the library should too:
- `#fff` should be treated the same as `#ffffff`
- `#f00` should be treated the same as `#ff0000`
- etc.

### System Info
- @mantine/core version: latest
- Browser: N/A (affects all environments)

---
Repository: /testbed
