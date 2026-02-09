# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the headings are not inheriting the custom font family as expected. The headings continue to use the default font instead of the specified custom font.

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

In this setup, body text correctly uses 'Inter', but headings (h1, h2, etc.) still use the default font family instead of inheriting 'Inter'.

### Expected behavior

When `fontFamily` is specified in the theme without an explicit `headings.fontFamily`, the headings should automatically inherit the custom `fontFamily` value. This was the previous behavior and makes sense as a default - if you set a font for your app, headings should use that font unless explicitly overridden.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
