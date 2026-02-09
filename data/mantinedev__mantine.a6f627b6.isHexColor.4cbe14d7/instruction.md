# Bug Report

### Describe the bug

Short hex color codes (3-digit format) are no longer being recognized as valid colors. When I try to use shorthand hex colors like `#fff` or `#000`, they are not being converted properly and the color functions fail to process them.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This should work but doesn't
const white = toRgba('#fff');
const black = toRgba('#000');
const red = toRgba('#f00');

// Only the 6-digit format works now
const whiteWorking = toRgba('#ffffff'); // This works
```

### Expected behavior

Short hex color codes (3-digit format) should be recognized and converted to RGBA just like the full 6-digit format. `#fff` should be treated the same as `#ffffff`, `#f00` should work like `#ff0000`, etc.

This is standard CSS behavior and was working before.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
