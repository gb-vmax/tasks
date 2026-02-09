# Bug Report

### Describe the bug

Component variants are not being applied correctly when the `unstyled` prop is set. It appears that variant classes are only applied when `unstyled` is `true`, which is the opposite of the expected behavior. When using a component with a variant but without the `unstyled` prop, the variant styling doesn't appear.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* This button has no variant styling applied */}
      <Button variant="filled">Click me</Button>
      
      {/* This button incorrectly shows variant styling */}
      <Button variant="filled" unstyled>Click me</Button>
    </>
  );
}
```

### Expected behavior

- Components with a `variant` prop should have the variant classes applied by default
- When `unstyled={true}` is set, variant classes should NOT be applied
- The current behavior seems to be inverted

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
