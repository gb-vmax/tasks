# Bug Report

### Describe the bug

There seems to be a syntax error in the Notification component that's preventing it from compiling. The interface definition appears to be nested incorrectly inside the prop type definition, which breaks the component's type structure.

### Reproduction

```tsx
import { Notification } from '@mantine/core';

function MyComponent() {
  return (
    <Notification
      color="blue"
      radius="md"
      onClose={() => console.log('closed')}
    >
      Test notification
    </Notification>
  );
}
```

When trying to use the Notification component with props like `color`, `radius`, or `onClose`, TypeScript throws errors about the prop types not being defined correctly.

### Expected behavior

The Notification component should accept the standard props (`onClose`, `color`, `radius`) without any TypeScript errors and render properly.

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x
- React version: 18.x

---
Repository: /testbed
