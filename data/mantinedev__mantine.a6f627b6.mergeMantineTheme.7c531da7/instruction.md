# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the headings are not inheriting the custom font family as expected. It seems like the font family inheritance logic for headings is not working correctly.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

<MantineProvider
  theme={{
    fontFamily: 'Inter, sans-serif'
  }}
>
  <App />
</MantineProvider>
```

In this case, the body text uses 'Inter' correctly, but headings (h1, h2, etc.) don't inherit this font family and fall back to the default theme font.

### Expected behavior

When `fontFamily` is specified in the theme without explicitly setting `headings.fontFamily`, the headings should automatically inherit the custom `fontFamily` value. This was the behavior in previous versions and makes sense as a default - you shouldn't need to duplicate the font family setting for headings unless you want them to be different.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
