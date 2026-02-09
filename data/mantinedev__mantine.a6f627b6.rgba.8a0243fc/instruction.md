# Bug Report

### Describe the bug

The `rgba()` function is producing incorrect opacity values when used with CSS variable colors and oklch colors. The transparency calculation appears to be inverted for `var()` colors, and there's also an issue with how alpha values are applied to oklch colors that already have an alpha channel.

### Reproduction

```js
import { rgba } from '@mantine/core';

// Case 1: CSS variable colors
// The transparency is inverted - expecting 30% opacity but getting 70% opacity
const result1 = rgba('var(--my-color)', 0.3);
// Returns: color-mix(in srgb, var(--my-color), transparent 30%)
// Expected: color-mix(in srgb, var(--my-color), transparent 70%)

// Case 2: oklch colors with existing alpha
// The alpha value is being added with a % sign when it shouldn't be
const result2 = rgba('oklch(0.5 0.2 180 / 0.8)', 0.5);
// Returns: oklch(0.5 0.2 180 / 0.5%)
// Expected: oklch(0.5 0.2 180 / 0.5)
```

### Expected behavior

1. For CSS variable colors with `color-mix`, the transparent percentage should be calculated as `(1 - alpha) * 100` so that when alpha is 0.3, we get 70% transparent (not 30%)
2. For oklch colors that already have an alpha channel, the replacement should not include a `%` sign since oklch alpha values are unitless (0-1 range)

### System Info

- @mantine/core version: latest
- Browser: All browsers supporting color-mix and oklch

---
Repository: /testbed
