# Bug Report

### Describe the bug

When creating a Portal component with a className prop, the portal node creation fails with a runtime error. The className string is being processed incorrectly - it's trying to call `.filter()` on a string before splitting it, which causes the application to crash.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function MyComponent() {
  return (
    <Portal className="my-custom-class another-class">
      <div>Portal content</div>
    </Portal>
  );
}
```

When this component renders, it throws an error because strings don't have a `.filter()` method.

### Expected behavior

The Portal should render successfully and apply the className to the portal container element. The classes should be properly split and added to the classList.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
