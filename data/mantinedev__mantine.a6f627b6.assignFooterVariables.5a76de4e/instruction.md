# Bug Report

### Describe the bug

The AppShell footer is not displaying correctly when using the `collapsed` prop. The footer appears to be hidden/transformed when it should be visible, and visible when it should be hidden. The behavior seems inverted from what's expected.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

function Demo() {
  const [collapsed, setCollapsed] = useState(false);
  
  return (
    <AppShell
      footer={{ height: 60, collapsed }}
    >
      <AppShell.Footer>
        Footer content
      </AppShell.Footer>
      <AppShell.Main>
        <button onClick={() => setCollapsed(!collapsed)}>
          Toggle Footer
        </button>
      </AppShell.Main>
    </AppShell>
  );
}
```

When `collapsed` is `false`, the footer is hidden instead of being shown. When `collapsed` is `true`, the footer appears instead of being hidden.

### Expected behavior

- When `collapsed={false}`, the footer should be visible
- When `collapsed={true}`, the footer should be hidden/collapsed

The current behavior appears to be the opposite of what's expected.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
