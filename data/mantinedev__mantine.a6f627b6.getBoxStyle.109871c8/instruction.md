# Bug Report

### Describe the bug

When using the `Box` component with both `style` and `vars` props, the `vars` are not being applied correctly. It seems like the `style` prop is overriding the `vars` instead of being merged properly.

### Reproduction

```jsx
import { Box } from '@mantine/core';

<Box
  vars={{
    '--box-color': 'red',
    '--box-size': '100px'
  }}
  style={{
    backgroundColor: 'blue'
  }}
>
  Content
</Box>
```

### Expected behavior

Both the CSS variables from `vars` and the inline styles from `style` should be applied to the component. The CSS variables should be available for use and not be overwritten by the style prop.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
