# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the headings don't inherit the custom font family as expected. The headings appear to be using a different font than the one specified in the theme configuration.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

<MantineProvider
  theme={{
    fontFamily: 'Inter, sans-serif',
  }}
>
  <App />
</MantineProvider>
```

In this setup, body text correctly uses "Inter" but headings (h1, h2, etc.) don't pick up the custom font family.

### Expected behavior

When `fontFamily` is set in the theme without explicitly defining `headings.fontFamily`, the headings should automatically inherit the custom `fontFamily` value. This is the expected behavior for maintaining consistent typography across the application.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
