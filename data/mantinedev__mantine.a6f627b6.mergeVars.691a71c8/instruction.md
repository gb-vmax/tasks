# Bug Report

### Describe the bug

When using component style overrides with CSS variables, the variable precedence is not working as expected. Variables defined at higher levels (like theme or component defaults) are incorrectly overriding variables passed as props, when it should be the other way around.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// Define a button with custom CSS variables
<Button
  vars={{
    root: {
      '--button-bg': 'red'
    }
  }}
>
  Click me
</Button>

// Expected: button background should be red (from props)
// Actual: button background uses theme default instead
```

The props-level variables are being overridden by theme-level variables, which breaks the expected cascading behavior. Variables passed directly to components should have the highest priority but they're being ignored.

### Expected behavior

CSS variables passed as props should take precedence over theme-level or default variables. The merge order should respect the component hierarchy, with the most specific (props) overriding the most general (theme defaults).

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
