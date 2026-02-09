# Bug Report

### Describe the bug

The `NativeScrollArea` component is not rendering children correctly. When passing valid React children (strings, numbers, or other primitive values), they are not being displayed in the modal. Only object-type children seem to work now.

### Reproduction

```jsx
import { Modal } from '@mantine/core';

function MyComponent() {
  return (
    <Modal opened onClose={() => {}}>
      Hello World
    </Modal>
  );
}

// The text "Hello World" doesn't render
```

Also happens with numbers and other primitive children:

```jsx
<Modal opened onClose={() => {}}>
  {42}
</Modal>

<Modal opened onClose={() => {}}>
  <div>This works</div>
  But this text doesn't render
</Modal>
```

### Expected behavior

All valid React children types (strings, numbers, elements, fragments, etc.) should render correctly inside modals, not just object-type children.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
