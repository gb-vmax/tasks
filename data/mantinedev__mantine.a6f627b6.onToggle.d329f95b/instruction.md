# Bug Report

### Describe the bug

The Popover component's toggle functionality is completely broken. When clicking the trigger element, the popover no longer opens or closes as expected. It seems like the toggle behavior has been inverted or disabled entirely.

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
1. Create a basic Popover component with a trigger button
2. Click the trigger button
3. Nothing happens - the popover doesn't open

Also noticed that when the `disabled` prop is set to `true`, clicking the trigger actually opens the popover, which is the opposite of what should happen.

### Expected behavior

- Clicking the trigger should toggle the popover open/closed
- When `disabled={true}` is set, clicking the trigger should do nothing
- The popover should work in controlled and uncontrolled modes

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
