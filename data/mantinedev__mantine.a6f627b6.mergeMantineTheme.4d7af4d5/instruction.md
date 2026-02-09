# Bug Report

### Describe the bug

When setting a custom `fontFamily` in the theme override without explicitly setting `headings.fontFamily`, the heading font family is not being inherited from the base `fontFamily` as expected. The headings continue to use the default font instead of the custom font family.

### Reproduction

```js
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        fontFamily: 'Custom Font, sans-serif'
      }}
    >
      {/* Headings don't use 'Custom Font' */}
      <h1>This should use Custom Font</h1>
    </MantineProvider>
  );
}
```

### Expected behavior

When `fontFamily` is specified in the theme override without a separate `headings.fontFamily`, the headings should automatically inherit the custom `fontFamily` value. This way, you don't have to specify the font twice.

### Current behavior

The headings don't inherit the custom `fontFamily` and continue using the default heading font.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
