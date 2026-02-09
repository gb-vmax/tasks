# Bug Report

### Describe the bug

When parsing hexadecimal color values with alpha channel (hexa format), the ColorPicker is not correctly extracting the RGB and alpha components from the string. The color values appear incorrect or completely wrong when using 4-character or 8-character hexa color codes.

### Reproduction

```js
import { parseHexa } from '@mantine/core';

// 4-character hexa format (e.g., #RGBA)
const color1 = parseHexa('#f00a');
// Expected: red color with alpha ~0.667
// Actual: incorrect color values returned

// 8-character hexa format (e.g., #RRGGBBAA)
const color2 = parseHexa('#ff0000cc');
// Expected: red color with alpha ~0.8
// Actual: incorrect alpha value extracted
```

### Expected behavior

The parser should correctly extract the RGB components and alpha channel from hexa color strings:
- For 4-character format `#RGBA`, it should parse the first 3 characters as RGB and the 4th as alpha
- For 8-character format `#RRGGBBAA`, it should parse the first 6 characters as RGB and the last 2 as alpha

### System Info

- @mantine/core version: latest
- Browser: Any

---
Repository: /testbed
