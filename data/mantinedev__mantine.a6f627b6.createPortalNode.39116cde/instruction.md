# Bug Report

### Describe the bug

When using the `Portal` component with a `className` prop that contains multiple CSS classes, the classes are not being applied correctly to the portal container. Instead of adding each class individually, it appears that the entire array is being passed to `classList.add()`.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function MyComponent() {
  return (
    <Portal className="my-class another-class third-class">
      <div>Portal content</div>
    </Portal>
  );
}
```

When inspecting the portal node in the DOM, the classes are not applied as expected.

### Expected behavior

The portal container should have all three classes (`my-class`, `another-class`, `third-class`) added to its `classList`. Each class should be applied individually.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
