# Bug Report

### Describe the bug

The `rgba()` function is producing incorrect color output when using CSS variables with alpha values. The transparency calculation seems inverted - colors appear more opaque when they should be transparent and vice versa.

### Reproduction

```js
import { rgba } from '@mantine/core';

// Using CSS variable
const result = rgba('var(--color-primary)', 0.5);
console.log(result);
// Expected: color-mix(in srgb, var(--color-primary), transparent 50%)
// Actual: color-mix(in srgb, var(--color-primary), transparent 50%)

// With alpha = 0.2 (should be 80% transparent)
const result2 = rgba('var(--color-primary)', 0.2);
console.log(result2);
// The transparency percentage doesn't match the expected behavior
```

When passing an alpha value of 0.2, I expect the color to be mostly transparent (80% transparent), but the output seems to have the transparency inverted.

Also noticed that `alpha: 1` (fully opaque) now returns the fallback color `rgba(0, 0, 0, 1)` instead of the actual color, which seems wrong.

### Expected behavior

- `rgba('var(--color)', 0.5)` should produce 50% transparency
- `rgba('var(--color)', 0.2)` should produce 80% transparency (mostly transparent)
- `rgba('var(--color)', 1)` should produce a fully opaque color, not a fallback

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
