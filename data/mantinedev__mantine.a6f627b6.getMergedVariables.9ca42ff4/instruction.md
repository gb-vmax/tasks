# Bug Report

### Describe the bug

When using a custom `cssVariablesResolver` in `MantineProvider`, the custom CSS variables are not being applied correctly. It seems like the custom resolver is being called without the theme object, and even when it returns values, they're being overridden by the default resolver instead of the other way around.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const customResolver = (theme) => ({
  variables: {
    '--custom-color': '#ff0000',
  },
  light: {},
  dark: {},
});

function App() {
  return (
    <MantineProvider cssVariablesResolver={customResolver}>
      {/* Custom variables are not applied */}
      <div style={{ color: 'var(--custom-color)' }}>
        This should be red but isn't
      </div>
    </MantineProvider>
  );
}
```

### Expected behavior

The custom CSS variables from `cssVariablesResolver` should be applied and take precedence over the default variables. The resolver function should also receive the theme object as a parameter so it can generate variables based on the current theme.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
