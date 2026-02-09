# Bug Report

### Describe the bug

The `useDisclosure` hook's `open` handler is not working correctly - it sets the state to `false` instead of `true`. When calling the `open()` function, the disclosure state remains closed instead of opening.

### Reproduction

```jsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { open, close, toggle }] = useDisclosure(false);
  
  return (
    <div>
      <p>State: {opened ? 'opened' : 'closed'}</p>
      <button onClick={open}>Open</button>
    </div>
  );
}
```

When clicking the "Open" button, the state remains `closed` instead of changing to `opened`.

### Expected behavior

Calling `open()` should set the disclosure state to `true`, making `opened` equal to `true`.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
