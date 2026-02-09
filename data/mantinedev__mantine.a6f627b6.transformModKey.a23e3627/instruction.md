# Bug Report

### Describe the bug

The `data-` attribute modifier prefix is not being applied correctly to Box components. Instead of getting `data-my-mod`, attributes are being generated with double dashes like `data--my-mod`, and the check for existing `data-` prefixes seems to be broken.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// Expected: data-active attribute
// Actual: data--active attribute
<Box mod={{ active: true }}>Content</Box>

// Expected: data-disabled (should keep existing prefix)
// Actual: data--data-disabled (double prefix added)
<Box mod={{ 'data-disabled': true }}>Content</Box>
```

When inspecting the DOM, the attributes have incorrect prefixes with double dashes.

### Expected behavior

- Modifier keys without `data-` prefix should get `data-` prepended (e.g., `active` → `data-active`)
- Modifier keys that already start with `data-` should remain unchanged (e.g., `data-disabled` → `data-disabled`)

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
