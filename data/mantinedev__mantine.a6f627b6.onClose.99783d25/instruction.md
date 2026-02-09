# Bug Report

### Describe the bug

The Popover component is not closing properly when `onClose` is called. Instead of closing, the popover remains open or behaves unexpectedly. This makes it impossible to dismiss popovers through the normal close mechanisms.

### Reproduction

```jsx
import { Popover, Button } from '@mantine/core';

function Demo() {
  return (
    <Popover>
      <Popover.Target>
        <Button>Toggle popover</Button>
      </Popover.Target>
      <Popover.Dropdown>
        Popover content
      </Popover.Dropdown>
    </Popover>
  );
}
```

Steps to reproduce:
1. Open the popover by clicking the target button
2. Try to close it by clicking outside or using any close mechanism
3. The popover stays open instead of closing

### Expected behavior

The popover should close when `onClose` is triggered (e.g., clicking outside, pressing ESC, or calling the close function programmatically).

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox/Safari

---
Repository: /testbed
