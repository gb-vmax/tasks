# Bug Report

### Describe the bug

The `toggle` function from `useDisclosure` hook is not working correctly - it doesn't actually toggle the state. When called, the opened state remains unchanged instead of switching between true and false.

### Reproduction

```jsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { toggle }] = useDisclosure(false);
  
  return (
    <div>
      <p>State: {opened ? 'open' : 'closed'}</p>
      <button onClick={toggle}>Toggle</button>
    </div>
  );
}
```

When clicking the toggle button, the state stays at its current value (either always open or always closed) instead of alternating between the two states.

### Expected behavior

Calling `toggle()` should switch the `opened` state from `true` to `false` or from `false` to `true`. If the modal/drawer/etc is closed, it should open. If it's open, it should close.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
