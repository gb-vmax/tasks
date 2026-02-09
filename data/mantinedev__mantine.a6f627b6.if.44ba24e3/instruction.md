# Bug Report

### Describe the bug

The `colorsTuple` function is not handling array inputs correctly. When passing an array of color values, the function appears to be dropping the last element from the array instead of returning the full array as expected.

### Reproduction

```js
import { colorsTuple } from '@mantine/core';

// Pass an array with 10 color shades
const colors = colorsTuple([
  '#fff0f0',
  '#ffe0e0',
  '#ffd0d0',
  '#ffc0c0',
  '#ffb0b0',
  '#ffa0a0',
  '#ff9090',
  '#ff8080',
  '#ff7070',
  '#ff6060'
]);

console.log(colors.length); // Expected: 10, but getting 9
console.log(colors[9]); // Expected: '#ff6060', but getting undefined
```

### Expected behavior

When an array is passed to `colorsTuple`, it should return the complete array with all elements intact. The function should preserve all 10 color values that are provided.

### System Info

- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
