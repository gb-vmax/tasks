# Bug Report

### Describe the bug

When using floating elements with RTL (right-to-left) direction, the positioning is not being flipped correctly. The floating element appears on the wrong side when `dir="rtl"` is set.

### Reproduction

```jsx
import { Popover } from '@mantine/core';

function Demo() {
  return (
    <div dir="rtl">
      <Popover position="right">
        <Popover.Target>
          <Button>Target</Button>
        </Popover.Target>
        <Popover.Dropdown>
          Content
        </Popover.Dropdown>
      </Popover>
    </div>
  );
}
```

### Expected behavior

When `dir="rtl"` is set, positions like `"right"` should be flipped to `"left"` and vice versa. The floating element should appear on the opposite side to account for the RTL layout.

Currently, the popover appears on the right side even though it should be flipped to the left in RTL mode.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: Any

---
Repository: /testbed
