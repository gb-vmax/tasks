# Bug Report

### Describe the bug

When using `PopoverTarget` in uncontrolled mode, the popover doesn't toggle when clicking on elements that don't have their own `onClick` handler. The toggle functionality only works if the child component has an `onClick` prop defined.

### Reproduction

```jsx
import { Popover } from '@mantine/core';

function Demo() {
  return (
    <Popover>
      <Popover.Target>
        <Button>Click me</Button>
      </Popover.Target>
      <Popover.Dropdown>
        Popover content
      </Popover.Dropdown>
    </Popover>
  );
}
```

If the `Button` component doesn't have its own `onClick` handler, clicking it won't toggle the popover open/closed.

However, if you add an `onClick` to the button:

```jsx
<Button onClick={() => console.log('clicked')}>Click me</Button>
```

Then the popover works as expected.

### Expected behavior

The popover should toggle on click regardless of whether the target element has its own `onClick` handler or not. The toggle behavior should work for any clickable element used as a target.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
