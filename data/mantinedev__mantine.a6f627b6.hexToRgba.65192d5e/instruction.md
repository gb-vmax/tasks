# Bug Report

### Describe the bug

When using hex colors with alpha channel (8-digit hex format like `#RRGGBBAA`), the alpha value is being extracted from the wrong position in the string. The function appears to be reading the alpha from the beginning of the hex string instead of from the end where it should be.

Additionally, there seems to be an issue with 3-digit shorthand hex colors where the green channel is being duplicated incorrectly.

### Reproduction

```js
// 8-digit hex with alpha
const color1 = toRgba('#FF0000FF'); // Should have full opacity (alpha = 1)
// But alpha is being read from 'FF' at the start instead of 'FF' at the end

// 3-digit shorthand hex
const color2 = toRgba('#F0A'); 
// Green channel gets wrong value due to incorrect index
```

### Expected behavior

For 8-digit hex colors (`#RRGGBBAA`), the alpha channel should be extracted from the last 2 characters (positions 6-8), not the first 2 characters.

For 3-digit shorthand hex colors (`#RGB`), each character should be properly duplicated to form the full 6-digit representation.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
