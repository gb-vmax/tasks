# Bug Report

### Describe the bug

I'm experiencing an issue with the `AppShell` component where the header offset is being set incorrectly when the header is collapsed. The offset behavior seems to be inverted based on the layout mode.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      header={{ 
        height: { base: 60, sm: 80 },
        collapsed: true 
      }}
      layout="default" // non-fixed mode
    >
      <AppShell.Header>Header</AppShell.Header>
      <AppShell.Main>Content</AppShell.Main>
    </AppShell>
  );
}
```

When the header is collapsed in a non-fixed layout mode, the header offset is being set to `0px !important`, which causes layout issues. This appears to be backwards - the offset should be cleared for fixed layouts, not for default/static layouts.

Additionally, there seems to be an issue with how the base header height is being applied. The height variable is set even when `shouldOffset` is false, which can cause unexpected spacing.

### Expected behavior

- When header is collapsed in fixed mode: offset should be cleared
- When header is collapsed in non-fixed mode: offset should remain as is
- Base header height should only be set when offset is needed

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
