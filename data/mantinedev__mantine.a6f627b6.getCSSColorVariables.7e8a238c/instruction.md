# Bug Report

### Describe the bug

I'm experiencing an issue with color variable generation in the theme system. When using higher primary shade values (like 8 or 9), the hover states for filled variants appear to be using lighter shades instead of darker ones, which makes the hover effect look incorrect.

Additionally, the light variant text color seems to be clamped incorrectly - when using lower primary shade values, it appears to be selecting the wrong shade for text color.

### Reproduction

```tsx
import { MantineProvider, Button } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{
      primaryShade: 9
    }}>
      <Button color="blue">Hover me</Button>
    </MantineProvider>
  );
}
```

When hovering over the button, the hover color appears lighter than the base color instead of darker. Expected behavior would be that the hover state uses a darker shade (shade 8 when primary is 9).

Similarly, with a low primary shade value:

```tsx
<MantineProvider theme={{
  primaryShade: 3
}}>
  <Button variant="light" color="blue">Light variant</Button>
</MantineProvider>
```

The text color for the light variant doesn't look right - it seems to be using an incorrect shade value.

### Expected behavior

- Filled variant hover states should use a darker shade than the base color
- Light variant text colors should be properly calculated for all primary shade values

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
