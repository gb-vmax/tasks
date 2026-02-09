# Bug Report

### CSS Variables Not Being Generated Correctly

I'm experiencing an issue where CSS variables for component sizes are being generated with incorrect names. It seems like the variable naming has broken and is producing malformed variable names.

### Reproduction

When using components with size variants, the CSS variables that should be generated are not matching the expected format. For example:

```jsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{
      spacing: {
        xs: '0.5rem',
        sm: '0.75rem',
        md: '1rem',
        lg: '1.5rem',
        xl: '2rem'
      }
    }}>
      {/* Component usage */}
    </MantineProvider>
  );
}
```

### Expected behavior

CSS variables should be generated as:
- `--mantine-spacing-xs`
- `--mantine-spacing-sm`
- `--mantine-spacing-md`
- etc.

### Actual behavior

The generated CSS variables appear to have the wrong format and don't reference the actual size values from the theme configuration. This breaks styling for components that rely on these CSS variables.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
