# Bug Report

### Describe the bug

The `useDisclosure` hook's `open` handler doesn't actually open the disclosure state. When calling the `open()` function returned by the hook, the state remains closed instead of changing to `true`.

### Reproduction

```jsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { open, close, toggle }] = useDisclosure(false);
  
  return (
    <div>
      <p>State: {opened ? 'Open' : 'Closed'}</p>
      <button onClick={open}>Open</button>
      <button onClick={close}>Close</button>
    </div>
  );
}
```

When clicking the "Open" button, the state stays as "Closed" instead of changing to "Open".

### Expected behavior

Calling `open()` should set the disclosure state to `true`, making `opened` become `true` and triggering a re-render.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
