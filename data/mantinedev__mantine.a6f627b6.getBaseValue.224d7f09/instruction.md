# Bug Report

### Describe the bug

I'm having issues with responsive style props when passing object values. When I try to use an object with a `base` property to define responsive styles, the base value doesn't seem to be applied correctly. The styles just don't show up at all.

### Reproduction

```js
import { Box } from '@mantine/core';

// This doesn't work - base value is not applied
<Box
  style={{
    padding: {
      base: '20px',
      sm: '30px',
      md: '40px'
    }
  }}
>
  Content
</Box>
```

The base padding value should be applied, but nothing happens. If I use a simple string value like `padding: '20px'` it works fine, but as soon as I try to use an object with responsive values including a `base` property, it breaks.

### Expected behavior

The `base` value should be applied as the default/fallback style, with the other breakpoint values overriding it at their respective screen sizes.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
