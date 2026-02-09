# Bug Report

### Describe the bug

I'm getting unexpected errors when trying to use MantineProvider with valid theme configurations. The provider throws errors claiming my theme configuration is invalid, even though I'm using standard color names and valid shade values.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider
      theme={{
        primaryColor: 'blue',
        primaryShade: 6,
      }}
    >
      {/* App content */}
    </MantineProvider>
  );
}
```

This throws an error about invalid primary color, even though 'blue' is a default Mantine color.

Similarly, using a valid shade value:

```tsx
<MantineProvider
  theme={{
    primaryColor: 'violet',
    primaryShade: 5,
  }}
>
  {/* App content */}
</MantineProvider>
```

Also throws an error about invalid primary shade.

### Expected behavior

The MantineProvider should accept valid color names from the default color palette and shade values between 0-9 without throwing errors. These are documented as valid configuration options.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
