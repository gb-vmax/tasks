# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props where breakpoint values are not being resolved correctly. When I pass an object with breakpoint-specific values (like `{ base: 'value1', md: 'value2' }`), the component seems to be using the breakpoint name itself instead of the actual value from the object.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      p={{ base: 'md', lg: 'xl' }}
      m={{ base: '10px', sm: '20px' }}
    >
      Content here
    </Box>
  );
}
```

When rendering this component, instead of applying the padding values 'md' and 'xl' at their respective breakpoints, it appears to be using the breakpoint keys themselves ('base', 'lg', etc.) as the values.

### Expected behavior

The component should extract and apply the correct values from the responsive object based on the current breakpoint. For example:
- At the `base` breakpoint, padding should be `'md'`
- At the `lg` breakpoint, padding should be `'xl'`

Instead, it seems like the breakpoint name is being returned rather than looking up the value in the object.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
