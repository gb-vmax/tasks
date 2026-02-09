# Bug Report

### Describe the bug

When using components with the `unstyled` prop set to `true`, variant classes are unexpectedly being applied. The variant styling should be completely removed when `unstyled={true}`, but instead the variant-specific classes are still being added to the component.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This button should have no variant classes applied
<Button unstyled variant="filled">
  Click me
</Button>

// Expected: No variant classes in the DOM
// Actual: Classes like "button--filled" are still being applied
```

The issue occurs with any component that supports both `variant` and `unstyled` props. When `unstyled` is set to `true`, all variant-specific styling should be stripped, but the variant classes are still being added.

### Expected behavior

When `unstyled={true}` is set on a component, no variant classes should be applied regardless of what `variant` prop is passed. The component should render without any variant-specific styling.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
