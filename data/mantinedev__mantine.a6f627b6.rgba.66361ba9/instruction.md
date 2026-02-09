# Bug Report

### Describe the bug

The `rgba()` function is producing incorrect transparency values when used with CSS custom properties (CSS variables). The transparency is inverted - when I pass an alpha value of 0.5, I'm getting 50% transparency instead of 50% opacity.

### Reproduction

```js
import { rgba } from '@mantine/core';

// Using CSS variable
const result = rgba('var(--my-color)', 0.5);
console.log(result);
// Expected: color-mix(in srgb, var(--my-color), transparent 50%)
// Actual: color-mix(in srgb, var(--my-color), transparent 50%)
// But the visual result is inverted - 50% transparent instead of 50% opaque

// Another example with alpha 0.2 (should be mostly opaque)
const result2 = rgba('var(--my-color)', 0.2);
// This gives 20% transparency but should give 80% transparency (20% opacity)
```

### Expected behavior

When calling `rgba('var(--my-color)', 0.5)`, the color should be 50% opaque (50% transparent). Currently it seems like the alpha value is being used directly as the transparency percentage instead of being converted properly.

For alpha = 0.5, I expect the element to be semi-transparent (50% see-through).
For alpha = 0.2, I expect the element to be mostly opaque (only 20% see-through).

### Additional context

This only affects CSS variables passed to the `rgba()` function. Regular color strings seem to work fine. The issue appears to be with how the `color-mix()` function is being generated.

---
Repository: /testbed
