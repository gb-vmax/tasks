# Bug Report

### Describe the bug

The `AppShell` component is not correctly handling responsive size configurations. When passing a responsive size object with only a `base` property, it's being treated as a responsive size when it should be treated as a regular size value.

### Reproduction

```tsx
import { AppShell } from '@mantine/core';

function App() {
  return (
    <AppShell
      navbar={{
        width: { base: 300 },
        breakpoint: 'sm'
      }}
    >
      {/* content */}
    </AppShell>
  );
}
```

### Expected behavior

When a size object contains only the `base` property (like `{ base: 300 }`), it should be treated as a non-responsive size and the logic should handle it accordingly. The component should recognize that this is not truly a responsive configuration since there are no breakpoint-specific values.

Currently, the size validation logic returns early and doesn't check whether the object only contains a `base` key, causing incorrect behavior in the media styles generation.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
