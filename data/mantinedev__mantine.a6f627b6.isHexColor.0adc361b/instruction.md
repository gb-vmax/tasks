# Bug Report

### Describe the bug

The `toRgba` function is accepting invalid hex color strings that should be rejected. Specifically, hex colors with odd-length strings (like 5 or 7 characters after the `#`) are being validated as correct when they should fail validation.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// These should be rejected but are currently accepted:
toRgba('#12345');   // 5 hex digits - invalid
toRgba('#1234567'); // 7 hex digits - invalid

// Valid formats that should work:
toRgba('#123');     // 3 hex digits - valid
toRgba('#1234');    // 4 hex digits (with alpha) - valid
toRgba('#123456');  // 6 hex digits - valid
toRgba('#12345678'); // 8 hex digits (with alpha) - valid
```

### Expected behavior

The color validation should only accept standard hex color formats:
- 3 digits: `#RGB`
- 4 digits: `#RGBA`
- 6 digits: `#RRGGBB`
- 8 digits: `#RRGGBBAA`

Invalid formats with 5 or 7 hex digits should be rejected and not processed.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
