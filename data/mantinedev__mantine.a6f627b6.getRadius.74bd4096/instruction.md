# Bug Report

### Describe the bug

The `getRadius` utility function is returning incorrect CSS variable names for radius values. When passing a radius size, it's using `--mantine-radius-default` as the variable prefix instead of `--mantine-radius`, which causes the wrong radius values to be applied to components.

### Reproduction

```tsx
import { getRadius } from '@mantine/core';

// This should return 'var(--mantine-radius-sm)'
// but instead returns 'var(--mantine-radius-default-sm)'
const radius = getRadius('sm');
console.log(radius);

// Expected: 'var(--mantine-radius-sm)'
// Actual: 'var(--mantine-radius-default-sm)'
```

When using components with the `radius` prop:

```tsx
<Button radius="sm">Click me</Button>
```

The button is trying to use a non-existent CSS variable `--mantine-radius-default-sm` instead of the correct `--mantine-radius-sm`, causing the radius to not be applied correctly.

### Expected behavior

The `getRadius` function should generate CSS variable names with the `--mantine-radius-` prefix (e.g., `--mantine-radius-sm`, `--mantine-radius-md`) not `--mantine-radius-default-` prefix.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
