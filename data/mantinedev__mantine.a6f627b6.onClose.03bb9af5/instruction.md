# Bug Report

### Describe the bug

The `Notification` component appears to have a syntax error in its TypeScript interface definition. When trying to use the component, I'm getting compilation errors about the interface structure.

### Reproduction

```tsx
import { Notification } from '@mantine/core';

function MyComponent() {
  return (
    <Notification
      onClose={() => console.log('closed')}
      color="blue"
      radius="md"
    >
      Test notification
    </Notification>
  );
}
```

When trying to compile this, TypeScript throws errors about the `NotificationProps` interface definition being malformed.

### Expected behavior

The component should compile without errors and the `NotificationProps` interface should be properly defined with the `onClose`, `color`, and `radius` properties available.

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x
- Framework: React 18

---
Repository: /testbed
