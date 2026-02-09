# Bug Report

### Describe the bug

I'm having an issue with the color parsing functionality. When I try to use 3-character hex color codes (shorthand notation like `#fff` or `#abc`), they are not being recognized as valid colors anymore.

### Reproduction

```js
// These shorthand hex colors are not working
toRgba('#fff')  // Should convert to rgba(255, 255, 255, 1) but fails
toRgba('#abc')  // Should convert to rgba(170, 187, 204, 1) but fails
toRgba('#f0f')  // Should convert to rgba(255, 0, 255, 1) but fails

// Only 6-character hex codes work now
toRgba('#ffffff')  // This works fine
toRgba('#aabbcc')  // This works fine
```

### Expected behavior

Both 3-character shorthand hex codes (like `#fff`) and 6-character hex codes (like `#ffffff`) should be accepted and converted properly to RGBA values. The shorthand notation is standard CSS and should be supported.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
