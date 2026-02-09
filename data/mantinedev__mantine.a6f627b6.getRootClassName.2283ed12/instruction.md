# Bug Report

### Describe the bug

When using custom selectors with the styles API, the root className is being incorrectly applied to non-root elements. This causes styling issues where classes meant only for the root element are being added to child elements with selectors that partially match the root selector.

### Reproduction

```tsx
import { Box } from '@mantine/core';

// Component with custom selectors
<Box
  classNames={{
    root: 'my-root-class',
    rootItem: 'my-item-class'  // This incorrectly receives the root className
  }}
/>
```

The issue occurs when you have selectors like:
- `root` (root selector)
- `rootItem` or `itemRoot` (non-root selector that contains "root")

The non-root selector incorrectly gets the root className applied because the selector matching logic is too permissive.

### Expected behavior

Only the exact root selector should receive the root className. Selectors that merely contain the root selector string as a substring (like `rootItem`, `itemRoot`, etc.) should not be treated as root elements.

For example:
- `root` selector → should get root className ✓
- `rootItem` selector → should NOT get root className ✗ (currently does)
- `itemRoot` selector → should NOT get root className ✗ (currently does)

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
