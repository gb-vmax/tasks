# Bug Report

### Describe the bug

Portal components are not rendering with the correct CSS classes. When passing a `className` prop to a Portal, the classes are not being applied to the portal node in the DOM.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function App() {
  return (
    <Portal className="my-custom-class another-class">
      <div>Portal content</div>
    </Portal>
  );
}
```

When inspecting the DOM, the portal node should have `my-custom-class` and `another-class` applied, but the classes are missing.

### Expected behavior

The portal node should have all the classes from the `className` prop applied to it. The classes should be visible in the DOM when inspecting the element.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
