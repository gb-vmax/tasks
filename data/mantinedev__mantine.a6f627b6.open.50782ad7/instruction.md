# Bug Report

### Describe the bug

After a recent update, the `useDisclosure` hook seems to have a syntax/formatting issue. When trying to import and use the hook in my component, I'm getting unexpected behavior where the hook doesn't work at all.

### Reproduction

```jsx
import { useDisclosure } from '@mantine/hooks';

function MyComponent() {
  const [opened, { open, close, toggle }] = useDisclosure(false);
  
  return (
    <div>
      <button onClick={open}>Open</button>
      <button onClick={close}>Close</button>
      <button onClick={toggle}>Toggle</button>
      <p>State: {opened ? 'opened' : 'closed'}</p>
    </div>
  );
}
```

The component fails to render and I'm seeing errors related to the hook import. It looks like there might be a problem with the hook's structure or exports.

### Expected behavior

The `useDisclosure` hook should work as documented, providing handlers for `open`, `close`, and `toggle` operations along with the current state.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Node version: 18.x

---
Repository: /testbed
