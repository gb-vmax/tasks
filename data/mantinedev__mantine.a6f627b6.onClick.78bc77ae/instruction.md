# Bug Report

### Describe the bug

When using `PopoverTarget` with a child component that doesn't have an `onClick` handler, the popover no longer toggles on click. The popover only opens/closes when the child component explicitly defines an `onClick` prop, even if it's just a placeholder function.

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

In this example, clicking the button does nothing - the popover doesn't open. However, if I add an `onClick` handler to the Button:

```jsx
<Button onClick={() => {}}>Toggle popover</Button>
```

Then it works as expected.

### Expected behavior

The popover should toggle when clicking the target element, regardless of whether the child component has its own `onClick` handler defined. This was working fine in previous versions.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
