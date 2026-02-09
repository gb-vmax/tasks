# Bug Report

### Describe the bug

I'm experiencing an issue with the `mod` prop on Box components. When passing data attributes that already have the `data-` prefix, the resulting HTML attributes are being incorrectly transformed. Instead of preserving the original attribute name, it appears the prefix is being stripped off.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box mod={{ 'data-active': true }}>
      Content
    </Box>
  );
}
```

When inspecting the rendered HTML, I expected to see `data-active` on the element, but instead I'm getting just `active` as the attribute name.

### Expected behavior

When a mod key already starts with `data-`, it should be kept as-is without any transformation. The component should render with the correct `data-active` attribute in the DOM.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
