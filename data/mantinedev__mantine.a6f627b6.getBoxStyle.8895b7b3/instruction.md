# Bug Report

### Describe the bug

I'm experiencing an issue with the `Box` component where `vars` (CSS variables) are not being applied correctly. It seems like the CSS variables passed through the `vars` prop are getting overridden or merged in the wrong order, causing styles to not render as expected.

### Reproduction

```tsx
import { Box } from '@mantine/core';

<Box
  style={{ color: 'red' }}
  vars={{ '--custom-color': 'blue' }}
  styleProps={{ fontSize: '16px' }}
>
  Content
</Box>
```

When inspecting the element, the CSS variables from `vars` don't seem to be applied properly, or they're being overridden by other style properties. The final computed styles are not what I would expect based on the props passed.

### Expected behavior

The `vars` prop should properly apply CSS variables to the Box component, and they should be merged correctly with `style` and `styleProps` without unexpected overrides. The order of style application should be predictable and consistent.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
