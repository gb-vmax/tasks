# Bug Report

### Describe the bug

I'm getting an unexpected error when trying to use a valid `primaryColor` in my MantineProvider theme configuration. The error says the primary color is invalid even though it's clearly defined in the colors object.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab']
  }
};

function App() {
  return (
    <MantineProvider theme={theme}>
      {/* App content */}
    </MantineProvider>
  );
}
```

### Expected behavior

The provider should accept the theme without throwing an error since `blue` is defined in the colors object. This used to work fine but now it's throwing an "Invalid primary color" error.

### Additional context

This seems to happen with any valid primaryColor configuration. Even using the default colors from Mantine causes this issue. The error appears immediately when the MantineProvider mounts.

---
Repository: /testbed
