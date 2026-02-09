# Bug Report

### Describe the bug

When using `AppShell` with responsive padding configuration, the padding values are not being applied correctly. The base padding value is ignored, and breakpoint-specific padding values (like `sm`, `md`, `lg`, etc.) are also not working as expected.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      padding={{
        base: 'md',
        sm: 'lg',
        md: 'xl'
      }}
    >
      <AppShell.Main>
        Content here
      </AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

- The `base` padding value should be applied as the default padding
- Breakpoint-specific padding values (`sm`, `md`, etc.) should override the base value at their respective breakpoints
- The component should render with proper padding at different screen sizes

### Actual behavior

The padding is not being applied correctly. The base padding doesn't seem to take effect, and the responsive breakpoint values are also not working properly.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
