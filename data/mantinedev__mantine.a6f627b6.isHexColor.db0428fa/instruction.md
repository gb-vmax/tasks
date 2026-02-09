# Bug Report

### Describe the bug

The `toRgba()` function is not correctly validating hex color codes. It's accepting invalid hex color strings that should be rejected, leading to unexpected behavior when trying to convert colors.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// These invalid hex colors are being accepted:
toRgba('#');  // Should fail but doesn't
toRgba('##');  // Should fail but doesn't
toRgba('#FFFFF');  // Should fail but doesn't
toRgba('FFFFFFF');  // Should fail but doesn't

// Valid colors that should work:
toRgba('#FFF');  // 3-digit hex
toRgba('#FFFFFF');  // 6-digit hex
toRgba('#FFFFFF80');  // 8-digit hex with alpha
```

### Expected behavior

The function should only accept valid hex color formats:
- 3-digit hex: `#FFF` or `FFF`
- 6-digit hex: `#FFFFFF` or `FFFFFF`
- 8-digit hex with alpha: `#FFFFFF80` or `FFFFFF80`

Invalid formats should be rejected and not processed.

### System Info
- @mantine/core version: latest
- Browser: N/A (affects all environments)

---
Repository: /testbed
