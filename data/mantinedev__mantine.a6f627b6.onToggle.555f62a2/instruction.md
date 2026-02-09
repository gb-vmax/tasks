# Bug Report

### Describe the bug

The Popover component stopped toggling open/closed when clicking the trigger. The popover appears to be completely non-functional - clicking the trigger element does nothing and the popover never opens.

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
1. Create a basic Popover component with a trigger and dropdown
2. Click the trigger button
3. Nothing happens - the popover doesn't open

### Expected behavior

Clicking the trigger should toggle the popover open/closed. The dropdown should appear when clicking the trigger for the first time, and close when clicking it again.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to have broken recently, as the same code was working fine before. The popover just doesn't respond to any clicks now.

---
Repository: /testbed
