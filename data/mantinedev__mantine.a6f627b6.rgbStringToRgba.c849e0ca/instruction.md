# Bug Report

### Describe the bug

The `toRgba` function is not handling RGB/RGBA color strings correctly. When passing a valid RGB color string, the alpha channel is being set incorrectly, resulting in transparent colors instead of opaque ones.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This should return { r: 255, g: 0, b: 0, a: 1 }
// But returns { r: 255, g: 0, b: 0, a: undefined }
const result = toRgba('rgb(255, 0, 0)');
console.log(result);
// Expected: { r: 255, g: 0, b: 0, a: 1 }
// Actual: { r: 255, g: 0, b: 0, a: undefined }
```

The issue is that RGB strings without an explicit alpha value are being converted with `a: undefined` instead of defaulting to `a: 1` (fully opaque). This causes colors to render as transparent when they should be opaque.

### Expected behavior

RGB color strings without an alpha channel should default to `a: 1` (fully opaque). Only RGBA strings with an explicit alpha value should use that value.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
