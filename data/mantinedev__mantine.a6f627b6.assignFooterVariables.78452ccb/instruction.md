# Bug Report

### Describe the bug

I'm experiencing issues with the AppShell footer behavior when using the `collapsed` prop. The footer offset and transform CSS variables are being applied incorrectly, causing the footer to display when it should be hidden and vice versa.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      footer={{ height: 60, collapsed: false }}
    >
      <AppShell.Footer>
        Footer content
      </AppShell.Footer>
      <AppShell.Main>
        Main content
      </AppShell.Main>
    </AppShell>
  );
}
```

When `collapsed` is set to `false`, the footer appears to have incorrect transform values applied. Similarly, when `collapsed` is `true`, the footer doesn't collapse as expected.

### Expected behavior

- When `footer.collapsed` is `false`, the footer should be visible and positioned correctly without any transform applied
- When `footer.collapsed` is `true`, the footer should be hidden with the appropriate transform
- The offset calculations should respect the `shouldOffset` parameter properly

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
