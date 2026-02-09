# Bug Report

### Describe the bug

The `toggle` function from `useDisclosure` hook is not working as expected. Instead of toggling the state between true and false, it always sets the state to false regardless of the current state.

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

Steps to reproduce:
1. Create a component using `useDisclosure`
2. Click the toggle button multiple times
3. The state stays false after the first click instead of alternating between true/false

### Expected behavior

The `toggle` function should switch the state from false to true and from true to false on each call. If the current state is `false`, calling `toggle()` should set it to `true`, and vice versa.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
