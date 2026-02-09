# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where custom `className` props are being applied to all component parts instead of just the root element. This is causing style conflicts and unexpected styling behavior throughout my components.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This className should only apply to the root element
<Button className="my-custom-class">
  Click me
</Button>
```

The `my-custom-class` is now being added to all internal elements of the Button component (label, loader, icon, etc.) instead of just the root wrapper element. This breaks component styling and causes CSS specificity issues.

### Expected behavior

The `className` prop should only be applied to the root element of the component, not propagated to all nested parts. Internal component elements should maintain their own isolated class names unless explicitly targeted through the `classNames` prop.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
