# Bug Report

### Describe the bug

I'm experiencing an issue with the Popover component where the onClick handler on PopoverTarget is being called twice. When I click on a popover target that has its own onClick handler, the handler gets executed two times instead of once.

### Reproduction

```jsx
import { Popover, Button } from '@mantine/core';

function Demo() {
  const handleClick = () => {
    console.log('Button clicked');
  };

  return (
    <Popover>
      <Popover.Target>
        <Button onClick={handleClick}>Toggle popover</Button>
      </Popover.Target>
      <Popover.Dropdown>
        Popover content
      </Popover.Dropdown>
    </Popover>
  );
}
```

When clicking the button, "Button clicked" is logged to the console twice. This causes any side effects in the onClick handler to be executed multiple times, which breaks functionality like form submissions, API calls, or state updates.

### Expected behavior

The onClick handler should only be called once per click event. The popover should toggle normally while respecting the custom onClick handler without duplicating the call.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox (happens in both)

---
Repository: /testbed
