# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the heading font family is not being inherited from the main `fontFamily` property as expected. The headings continue to use the default font instead of the custom one.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

<MantineProvider
  theme={{
    fontFamily: 'Inter, sans-serif'
  }}
>
  <h1>This heading should use Inter font</h1>
  <p>This text correctly uses Inter font</p>
</MantineProvider>
```

### Expected behavior

When only `fontFamily` is specified in the theme override (without explicitly setting `headings.fontFamily`), the headings should automatically inherit the custom font family. Currently, the headings are not picking up the custom font and continue using the default.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
