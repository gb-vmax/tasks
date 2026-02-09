# Bug Report

### Describe the bug

I'm experiencing an issue with CSS variable resolution in Mantine components. When using components with multiple theme names (component inheritance/composition), the CSS variables from parent components are being applied in the wrong order, causing styles to be overridden incorrectly.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// Create a component that extends another component with custom vars
const CustomButton = () => {
  return (
    <Button
      // Custom styling that should override base component vars
      styles={{
        root: {
          // These vars should take precedence but they don't
        }
      }}
    />
  );
};
```

When a component has multiple theme names in its hierarchy, the vars from components later in the theme name array are being overridden by earlier ones, which is the opposite of what should happen.

### Expected behavior

CSS variables should be resolved in the correct order, with child/extended component variables taking precedence over parent component variables. The theme name array should be processed so that the most specific component's vars override the more general ones.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
