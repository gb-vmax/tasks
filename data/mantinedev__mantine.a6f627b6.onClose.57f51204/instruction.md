# Bug Report

### Describe the bug

The Popover component's close functionality is broken. When trying to close an open popover, it remains open instead of closing. Additionally, attempting to close a disabled popover causes it to open unexpectedly.

### Reproduction

```jsx
import { Popover, Button } from '@mantine/core';

function Demo() {
  const [opened, setOpened] = useState(true);
  
  return (
    <Popover opened={opened} onChange={setOpened}>
      <Popover.Target>
        <Button>Toggle</Button>
      </Popover.Target>
      <Popover.Dropdown>
        <Button onClick={() => setOpened(false)}>Close</Button>
      </Popover.Dropdown>
    </Popover>
  );
}
```

Steps to reproduce:
1. Open a popover
2. Try to close it by clicking outside or calling the close handler
3. The popover stays open instead of closing

### Expected behavior

- Clicking outside an open popover should close it
- Calling the close handler should close an open popover
- Disabled popovers should not change state when attempting to close them

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
