# Bug Report

### Describe the bug

When using the `Portal` component with a string `target` selector that doesn't match any existing DOM element, the portal fails to render correctly. The component seems to break when the selector doesn't find a matching element in the document.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function App() {
  return (
    <Portal target="#non-existent-element">
      <div>This content should be portaled</div>
    </Portal>
  );
}
```

### Expected behavior

When the target selector doesn't match any element, the Portal should fall back to creating a new portal node and append it to the document body, allowing the content to render properly.

### Actual behavior

The portal content doesn't render at all when using a non-existent selector string as the target.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
