# Bug Report

### Describe the bug

The hex color conversion is producing incorrect output. When converting colors to hex format, the resulting hex strings are malformed with digits appearing in the wrong positions.

### Reproduction

```js
// Converting a color to hex format
const color = { h: 0, s: 100, v: 50, a: 1 };
const hexColor = hsvaToHex(color);

// Expected: #800000 (or similar valid hex)
// Actual: Malformed hex string with trailing zeros in wrong places
```

For example, single-digit hex values like `8` should be padded to become `08`, but instead they're being formatted incorrectly.

### Expected behavior

Hex color strings should be properly formatted with leading zeros for single-digit values. Each RGB component should be exactly 2 characters long.

For instance:
- `8` should become `08`
- `f` should become `0f`  
- `10` should remain `10`

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
