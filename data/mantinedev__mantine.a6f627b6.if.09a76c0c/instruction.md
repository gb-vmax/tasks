# Bug Report

### Describe the bug

The `isResponsiveSize` function in AppShell is incorrectly identifying non-object values as responsive sizes. When passing primitive values like numbers or strings to AppShell size props, they're being treated as responsive size objects instead of static sizes, which breaks the layout rendering.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      navbar={{ width: 300, breakpoint: 'sm' }}
      padding="md"
    >
      {/* Content */}
    </AppShell>
  );
}
```

When using a simple number value (like `300`) for width, the AppShell doesn't render correctly because the value is being misidentified as a responsive size object.

### Expected behavior

Primitive values (numbers, strings) should be recognized as static sizes, not responsive size objects. Only actual objects with breakpoint keys should be treated as responsive sizes.

For example:
- `300` → static size (not responsive)
- `{ base: 300, sm: 400 }` → responsive size
- `"md"` → static size (not responsive)

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
