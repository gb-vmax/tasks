# Bug Report

### Describe the bug

When using floating elements with `position` prop set to `left` or `left-*` variants, the positioning is not working correctly. The element appears to always position itself on the right side regardless of the specified position value.

### Reproduction

```jsx
import { Popover } from '@mantine/core';

function Demo() {
  return (
    <Popover position="left">
      <Popover.Target>
        <Button>Target</Button>
      </Popover.Target>
      <Popover.Dropdown>
        Content
      </Popover.Dropdown>
    </Popover>
  );
}
```

### Expected behavior

When `position="left"` is set, the popover/dropdown should appear on the left side of the target element. Similarly, `position="left-start"` and `position="left-end"` should position the element on the left with the appropriate alignment.

### Current behavior

The floating element always appears on the right side, even when explicitly setting `position="left"` or any left-based position variant.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to affect all components that use floating positioning (Popover, Tooltip, Menu, etc.) when trying to position them on the left side of the target.

---
Repository: /testbed
