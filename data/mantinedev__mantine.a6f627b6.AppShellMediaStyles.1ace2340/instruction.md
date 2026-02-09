# Bug Report

### Describe the bug

The `AppShellMediaStyles` component is not rendering inline styles correctly. After a recent update, the styles are no longer being applied to the component, causing the layout to break.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      navbar={{ width: 300, breakpoint: 'sm' }}
      header={{ height: 60 }}
    >
      <AppShell.Header>Header</AppShell.Header>
      <AppShell.Navbar>Navbar</AppShell.Navbar>
      <AppShell.Main>Content</AppShell.Main>
    </AppShell>
  );
}
```

When the component renders, the CSS variables and media queries that should be applied are missing, resulting in incorrect layout behavior. The navbar and header don't respond to breakpoints as expected.

### Expected behavior

The `AppShellMediaStyles` should properly inject inline styles with the correct selector, allowing the AppShell layout to work correctly across different screen sizes.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
