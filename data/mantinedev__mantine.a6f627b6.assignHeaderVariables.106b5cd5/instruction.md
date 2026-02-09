# Bug Report

### Describe the bug

I'm experiencing an issue with the AppShell component where the header height is not being applied correctly at different breakpoints. It seems like the responsive header height values are being ignored and only the base value is being used across all screen sizes.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  return (
    <AppShell
      header={{
        height: {
          base: 60,
          sm: 70,
          md: 80
        }
      }}
    >
      <AppShell.Header>Header content</AppShell.Header>
      <AppShell.Main>Main content</AppShell.Main>
    </AppShell>
  );
}
```

### Expected behavior

The header height should change based on the breakpoint:
- 60px for base (mobile)
- 70px for small screens
- 80px for medium screens and above

However, all breakpoints are using the same height value (the base value).

### Additional context

Also noticed that when using a collapsed header with `mode="static"`, the header offset is being set to `0px !important` even though the mode is not fixed. This seems like it might be related or a separate issue.

---
Repository: /testbed
