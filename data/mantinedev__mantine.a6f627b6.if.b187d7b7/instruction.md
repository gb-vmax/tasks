# Bug Report

### Describe the bug

The `colorsTuple` function is not working as expected when passed an array of colors. Instead of returning the array as a colors tuple, it seems to be creating an array filled with the input itself.

### Reproduction

```js
import { colorsTuple } from '@mantine/core';

// Passing an array of color shades
const colors = colorsTuple([
  '#fff5f5',
  '#ffe3e3',
  '#ffc9c9',
  '#ffa8a8',
  '#ff8787',
  '#ff6b6b',
  '#fa5252',
  '#f03e3e',
  '#e03131',
  '#c92a2a'
]);

console.log(colors);
// Expected: The array I passed in
// Actual: Something unexpected is returned
```

When I pass a string instead, it works fine and creates a tuple with 10 identical values. But when passing an array (which is the main use case for custom color shades), the behavior is broken.

### Expected behavior

When passing an array to `colorsTuple`, it should return that array as a `MantineColorsTuple`. When passing a single string, it should create an array of 10 identical values.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
