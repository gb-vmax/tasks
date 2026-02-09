# Bug Report

### Describe the bug

When using the `Portal` component with a string selector as the `target` prop, the portal fails to render if the target element doesn't exist in the DOM. Previously, the component would fall back to creating a portal node, but now it returns `undefined` and nothing renders.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function App() {
  return (
    <Portal target="#non-existent-element">
      <div>This content should render somewhere</div>
    </Portal>
  );
}
```

When the element with id `non-existent-element` doesn't exist, the portal content doesn't render at all. This breaks components that rely on portals when the target selector doesn't match any element.

### Expected behavior

The portal should create a fallback node and append it to the document body when the target selector doesn't find a matching element, allowing the portal content to still render.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
