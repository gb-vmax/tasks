# Bug Report

### Describe the bug

The `rem()` function is generating invalid CSS output when used with numeric values. Instead of wrapping the calculation in `calc()`, it's outputting raw multiplication syntax which browsers can't parse.

### Reproduction

```js
import { rem } from '@mantine/core';

// This generates invalid CSS
const spacing = rem(16);
// Expected: calc(1rem * var(--mantine-scale))
// Actual: 1rem * var(--mantine-scale)
```

When this value is applied to a CSS property, the browser ignores it because the multiplication operator isn't valid outside of a `calc()` function.

### Expected behavior

The `rem()` function should wrap scaled values in `calc()` so they produce valid CSS that browsers can interpret correctly.

### Additional context

This seems to affect all rem values except for `0rem`. The issue becomes apparent when inspecting computed styles - the properties using `rem()` values just don't apply at all.

---
Repository: /testbed
