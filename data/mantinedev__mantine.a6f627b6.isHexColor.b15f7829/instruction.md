# Bug Report

### Describe the bug

I'm having issues with hex color validation in my application. It seems like 3-digit hex colors (shorthand notation like `#FFF` or `#000`) are being rejected as invalid, even though they should be valid CSS color values.

### Reproduction

```js
// These shorthand hex colors are not being recognized as valid
const color1 = '#FFF'; // Should be valid
const color2 = '#000'; // Should be valid
const color3 = 'ABC';  // Should be valid (without #)

// Only 6-digit hex colors seem to work
const color4 = '#FFFFFF'; // This works
const color5 = '#000000'; // This works
```

When I try to use 3-digit hex colors with `toRgba()` or any color function, they're not being processed correctly. The validation is failing for shorthand hex notation.

### Expected behavior

Both 3-digit and 6-digit hex color formats should be accepted as valid:
- `#FFF` should be treated as `#FFFFFF`
- `#000` should be treated as `#000000`
- `#ABC` should be treated as `#AABBCC`

This is standard CSS behavior and was working in previous versions.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
