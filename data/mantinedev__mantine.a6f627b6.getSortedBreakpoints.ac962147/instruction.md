# Bug Report

### Describe the bug

I'm experiencing an issue with responsive breakpoint ordering in my Mantine components. It seems like breakpoints are not being applied in the correct order, causing my responsive layouts to behave unexpectedly.

### Reproduction

```jsx
import { Container } from '@mantine/core';

<Container
  size={{
    base: 'xs',
    sm: 'md',
    lg: 'xl'
  }}
>
  Content
</Container>
```

When I define breakpoints like this, they don't seem to be sorted correctly. The larger breakpoints are being applied before smaller ones, which completely breaks the responsive behavior.

### Expected behavior

Breakpoints should be sorted from smallest to largest (ascending order by pixel value) so that media queries cascade properly. The `base` breakpoint should apply first, then `sm`, then `lg`, etc.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
