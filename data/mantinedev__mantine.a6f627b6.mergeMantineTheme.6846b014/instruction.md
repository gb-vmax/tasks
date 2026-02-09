# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the heading font family is not being inherited from the main `fontFamily` property. This means headings continue to use the default font instead of the custom font specified in the theme.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        fontFamily: 'Custom Font, sans-serif'
      }}
    >
      <h1>This heading should use Custom Font</h1>
      <p>This paragraph uses Custom Font correctly</p>
    </MantineProvider>
  );
}
```

### Expected behavior

When `fontFamily` is set in the theme without explicitly setting `headings.fontFamily`, the headings should automatically inherit the custom font family. Both the paragraph and heading should display in "Custom Font".

### Actual behavior

The paragraph text uses the custom font correctly, but the heading continues to use the default heading font instead of inheriting from the `fontFamily` property.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
