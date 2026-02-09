# Bug Report

### Describe the bug

I'm experiencing incorrect color conversion when using 3-character hex colors (shorthand notation). The RGB values are being mapped incorrectly, causing colors to appear completely different from what they should be.

### Reproduction

```js
// Using shorthand hex notation
const color = toRgba('#f0a');

// Expected: { r: 255, g: 0, b: 170, a: 1 }
// Actual: RGB values are scrambled/incorrect
```

When I pass a 3-character hex color like `#f0a` (which should expand to `#ff00aa`), the resulting RGBA object has the wrong red, green, and blue values. It seems like the color channels are getting mixed up during the expansion process.

### Expected behavior

3-character hex colors should be properly expanded to their 6-character equivalents before conversion:
- `#f0a` → `#ff00aa` → `{ r: 255, g: 0, b: 170, a: 1 }`
- `#abc` → `#aabbcc` → `{ r: 170, g: 187, b: 204, a: 1 }`

The red, green, and blue channels should maintain their correct positions.

### Additional context

This also affects 8-character hex colors with alpha values - the alpha channel appears to be extracted from the wrong position in the string.

---
Repository: /testbed
