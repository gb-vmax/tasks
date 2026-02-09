# Bug Report

### Describe the bug

The `rgba()` function is not correctly handling transparency when used with CSS variables. When I try to apply an alpha value to a color defined as a CSS variable, the transparency is inverted - a higher alpha value makes the color more transparent instead of more opaque.

### Reproduction

```js
// Using a CSS variable color
const color = 'var(--my-color)';

// Trying to make it 30% opaque (alpha = 0.3)
const result = rgba(color, 0.3);

// Expected: color-mix(in srgb, var(--my-color), transparent 70%)
// Actual: color-mix(in srgb, var(--my-color), transparent 30%)
// This makes the color 70% opaque instead of 30% opaque
```

The issue is that when alpha is 0.3 (meaning 30% opaque), the function should mix with 70% transparent, but it's mixing with 30% transparent instead, resulting in the opposite effect.

### Expected behavior

When calling `rgba('var(--primary)', 0.3)`, the color should be 30% opaque (70% transparent). Currently it's producing the inverse, making it 70% opaque (30% transparent).

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
