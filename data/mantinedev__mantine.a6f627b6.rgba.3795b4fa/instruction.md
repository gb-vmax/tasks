# Bug Report

### Describe the bug

The `rgba()` function is producing incorrect transparency values when used with CSS custom properties (CSS variables). The transparency appears to be inverted - when I pass `alpha: 0.5` expecting 50% opacity, I'm getting 50% transparency instead (which looks like 50% opacity of transparent, not the color).

### Reproduction

```js
import { rgba } from '@mantine/core';

// Using CSS variable
const result = rgba('var(--my-color)', 0.3);
console.log(result);
// Expected: color-mix(in srgb, var(--my-color), transparent 70%)
// Actual: color-mix(in srgb, var(--my-color), transparent 30%)

// The color appears much more transparent than expected
// When alpha is 0.3 (30% opacity), the result looks almost fully transparent
// When alpha is 0.9 (90% opacity), the result is barely visible
```

### Expected behavior

When calling `rgba('var(--my-color)', 0.3)`, I expect the color to have 30% opacity (70% transparent). The `color-mix` function should mix with transparent at the correct percentage to achieve the desired alpha value.

### Additional context

This seems to affect all CSS variable colors. Regular hex colors and oklch colors might have similar issues but I haven't tested those extensively yet.

---
Repository: /testbed
