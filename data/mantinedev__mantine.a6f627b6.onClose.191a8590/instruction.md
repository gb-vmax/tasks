# Bug Report

### Describe the bug

The Popover component's close functionality seems to be broken. When trying to close an open popover, it doesn't close anymore. The popover stays open even when clicking outside or triggering the close action.

### Reproduction

```jsx
import { Popover, Button } from '@mantine/core';

function Demo() {
  const [opened, setOpened] = useState(false);
  
  return (
    <Popover opened={opened} onChange={setOpened}>
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
1. Click the button to open the popover
2. Try to close it by clicking outside or using any close mechanism
3. The popover remains open and won't close

### Expected behavior

The popover should close when clicking outside, pressing ESC, or when the close action is triggered. It worked fine in previous versions but now it just stays open indefinitely.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
