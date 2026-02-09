# Bug Report

### Describe the bug

The `useDisclosure` hook is not working correctly - the `close` and `toggle` handlers are behaving unexpectedly. When I call `close()`, the state doesn't actually close, and when I call `toggle()`, nothing happens at all.

### Reproduction

```jsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { open, close, toggle }] = useDisclosure(false);

  return (
    <div>
      <p>State: {opened ? 'opened' : 'closed'}</p>
      <button onClick={open}>Open</button>
      <button onClick={close}>Close</button>
      <button onClick={toggle}>Toggle</button>
    </div>
  );
}
```

Steps to reproduce:
1. Start with `opened` as `false`
2. Click the "Open" button - this works correctly
3. Click the "Close" button - the state remains `true` instead of changing to `false`
4. Click the "Toggle" button - nothing happens, state stays the same

### Expected behavior

- `close()` should set the state to `false`
- `toggle()` should flip the state between `true` and `false`

The `open()` handler seems to work fine, but the other two are broken.

---
Repository: /testbed
