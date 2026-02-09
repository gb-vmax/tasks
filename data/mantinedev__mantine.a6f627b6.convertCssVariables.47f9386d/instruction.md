# Bug Report

### Describe the bug

CSS variables for light color scheme are not being applied correctly in MantineProvider. When using custom CSS variables with both light and dark color schemes, the light scheme variables seem to be overridden or not properly generated.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

<MantineProvider
  theme={{
    cssVariablesResolver: (theme) => ({
      variables: {
        '--my-color': 'shared-value',
      },
      light: {
        '--my-color': 'light-value',
      },
      dark: {
        '--my-color': 'dark-value',
      },
    }),
  }}
>
  <App />
</MantineProvider>
```

When switching to light mode, the CSS variable `--my-color` doesn't get the value `'light-value'` as expected. It seems like the dark mode styles are taking precedence or the light mode selector isn't being generated properly.

### Expected behavior

The light color scheme variables should be applied when `data-mantine-color-scheme="light"` is set, and should not be overridden by dark mode styles.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
