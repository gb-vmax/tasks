# Bug Report

### Describe the bug

The AppShell aside offset is not being applied correctly when the aside is collapsed. The layout behaves incorrectly depending on the mode setting - in non-fixed mode, the offset remains when it should be cleared, and in fixed mode, the width is being set to 0px instead of clearing the offset.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  const [collapsed, setCollapsed] = useState(false);
  
  return (
    <AppShell
      aside={{
        width: { base: 300 },
        breakpoint: 'sm',
        collapsed: { mobile: collapsed }
      }}
    >
      <AppShell.Aside>Aside content</AppShell.Aside>
      <AppShell.Main>
        <button onClick={() => setCollapsed(!collapsed)}>
          Toggle Aside
        </button>
        Main content
      </AppShell.Main>
    </AppShell>
  );
}
```

When toggling the aside in non-fixed mode, the main content doesn't adjust properly - there's still an offset applied even though the aside is collapsed. In fixed mode, the behavior is also wrong but in a different way.

### Expected behavior

When the aside is collapsed:
- In fixed mode: the aside offset should be set to 0px
- In non-fixed mode: the aside width should be set to 0px

The main content area should properly expand to fill the space when the aside collapses.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
