# Bug Report

### Describe the bug

When using `PopoverTarget` in controlled mode with a custom `onClick` handler, the popover doesn't toggle anymore if the child component doesn't have an `onClick` prop. The toggle functionality seems to be completely broken when there's no `onClick` on the target element.

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

### Expected behavior

The popover should toggle when clicking the target button, regardless of whether the child component has its own `onClick` handler or not.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
