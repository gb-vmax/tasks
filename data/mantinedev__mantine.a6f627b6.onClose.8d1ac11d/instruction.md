# Bug Report

### Describe the bug

After a recent update, the Notification component is completely broken and won't compile. Getting syntax errors when trying to use the component in my application.

### Reproduction

```tsx
import { Notification } from '@mantine/core';

function MyComponent() {
  return (
    <Notification
      title="Test notification"
      onClose={() => console.log('closed')}
      color="blue"
      radius="md"
    >
      This is a test notification
    </Notification>
  );
}
```

The code above fails to compile with TypeScript errors about the interface definition.

### Expected behavior

The Notification component should render properly with the provided props (onClose, color, radius) without any compilation errors.

### System Info
- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
