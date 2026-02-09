# Bug Report

### Describe the bug

I'm experiencing an issue with the ColorPicker component where parsing the color `'transparent'` returns an unexpected alpha value. When I use `'transparent'` as a color value, it seems to be handled incorrectly.

### Reproduction

```js
import { parseColor } from '@mantine/core';

const result = parseColor('transparent');
console.log(result);
// Output: { h: 0, s: 0, v: 0, a: 0.5 }
// Expected: { h: 0, s: 0, v: 0, a: 0 }
```

The alpha channel is being set to 0.5 instead of 0, which doesn't match the CSS spec for the `transparent` keyword (which should be fully transparent, i.e., alpha = 0).

### Expected behavior

When parsing the `'transparent'` color keyword, the alpha value should be 0 (fully transparent), not 0.5.

### Additional context

This affects any component using the ColorPicker where `'transparent'` is passed as an initial value or updated value. The color appears semi-transparent instead of fully transparent.

---
Repository: /testbed
