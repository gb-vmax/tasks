# Bug Report

### Describe the bug

When using the Portal component with a CSS selector target that doesn't exist in the DOM, the portal content is not being rendered. It seems like the fallback behavior has changed and the portal just silently fails instead of creating a fallback container.

### Reproduction

```jsx
import { Portal } from '@mantine/core';

function MyComponent() {
  return (
    <Portal target="#non-existent-element">
      <div>This content should be rendered somewhere</div>
    </Portal>
  );
}
```

### Expected behavior

When the target selector doesn't match any element, the Portal should still render its content by creating a fallback container and appending it to the document body (or render directly to body). Currently, the content just disappears.

Also noticed similar issues when using `reuseTargetNode` - the shared portal node gets created but the content doesn't appear in the DOM.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
