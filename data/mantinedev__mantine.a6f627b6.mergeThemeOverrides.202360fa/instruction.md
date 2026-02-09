# Bug Report

### Describe the bug

When using multiple theme overrides with `MantineProvider`, the themes are being merged in the wrong order. Earlier theme overrides are taking precedence over later ones, which is the opposite of expected behavior.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const theme1 = {
  colors: {
    brand: ['#fff', '#eee']
  }
};

const theme2 = {
  colors: {
    brand: ['#000', '#111']
  }
};

// theme2 should override theme1, but theme1 values are used instead
<MantineProvider theme={[theme1, theme2]}>
  <App />
</MantineProvider>
```

### Expected behavior

When multiple theme overrides are provided, later themes should override earlier ones (left-to-right precedence). In the example above, `theme2` should take priority over `theme1`, so the brand colors should be `['#000', '#111']` but instead they remain `['#fff', '#eee']`.

This makes it difficult to compose themes properly, especially when trying to layer base themes with more specific overrides.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
