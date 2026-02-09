# Bug Report

### Describe the bug

After updating to the latest version, I'm getting an unexpected error when trying to use a valid theme configuration with MantineProvider. The error says my primary color is invalid even though it's clearly defined in the colors object.

### Reproduction

```jsx
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

This throws an error: "MantineProvider: Invalid theme.primaryColor..."

The same thing happens with primaryShade:

```jsx
const theme = {
  primaryColor: 'blue',
  primaryShade: 6,
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab']
  }
};
```

This also throws an error about invalid primaryShade even though 6 is a valid shade value (0-9).

### Expected behavior

The theme should be accepted without errors since both the primaryColor exists in the colors object and the primaryShade is within the valid range.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
