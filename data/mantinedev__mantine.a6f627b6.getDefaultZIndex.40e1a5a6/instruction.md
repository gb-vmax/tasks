# Bug Report

### Describe the bug

After a recent update, z-index values for overlays and modals seem to be off by 1 from what they should be. Components that previously had the correct stacking order are now rendering at unexpected z-index levels.

### Reproduction

```tsx
import { Modal } from '@mantine/core';

// Modal should have z-index of 200 (modal level)
// But it's now rendering with z-index of 201
<Modal opened={true}>
  Content
</Modal>
```

When inspecting the computed styles, all z-index values returned by the utility function are 1 higher than expected. For example:
- `app` level should be 100, but returns 101
- `modal` level should be 200, but returns 201
- `popover` level should be 300, but returns 301
- `overlay` level should be 400, but returns 401
- `max` level should be 9999, but returns 10000

### Expected behavior

Z-index values should match the defined elevation levels without any offset. The `getDefaultZIndex` utility should return the exact values defined in the elevations object.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
