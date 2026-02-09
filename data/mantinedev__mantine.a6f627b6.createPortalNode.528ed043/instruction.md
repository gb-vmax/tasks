# Bug Report

### Describe the bug

The Portal component is not applying CSS classes correctly when a `className` prop is provided. The portal node is created in the DOM but none of the specified classes are actually added to the element.

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

When inspecting the DOM, the portal div has `data-portal="true"` but the classes `my-custom-class` and `another-class` are missing.

Also noticed that when passing an `id` prop, it doesn't get set on the portal node either:

```jsx
<Portal id="my-portal" className="test-class">
  <div>Content</div>
</Portal>
```

The portal div in the DOM has no `id` attribute.

### Expected behavior

The portal node should have all the classes from the `className` prop applied to it, and the `id` attribute should be set when provided.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
