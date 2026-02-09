# Bug Report

### Describe the bug

The `useDisclosure` hook is behaving incorrectly - the `open()`, `close()`, and `toggle()` functions are doing the opposite of what they should do. When I call `open()`, it closes the disclosure, and when I call `close()`, it opens it. The `toggle()` function is also inverted.

### Reproduction

```tsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { open, close, toggle }] = useDisclosure(false);

  return (
    <div>
      <p>Opened: {opened ? 'true' : 'false'}</p>
      <button onClick={open}>Open</button>
      <button onClick={close}>Close</button>
      <button onClick={toggle}>Toggle</button>
    </div>
  );
}
```

Steps to reproduce:
1. Start with `useDisclosure(false)` (closed state)
2. Click the "Open" button
3. The state remains `false` instead of changing to `true`
4. Click the "Close" button
5. Now the state changes to `true` (the opposite of what it should do)

The toggle function also does the reverse - it closes when opened and opens when closed.

### Expected behavior

- `open()` should set the state to `true`
- `close()` should set the state to `false`
- `toggle()` should switch between `true` and `false` correctly
- The callbacks `onOpen` and `onClose` should be called at the appropriate times

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
