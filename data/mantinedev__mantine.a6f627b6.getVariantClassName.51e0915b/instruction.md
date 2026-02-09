# Bug Report

### Describe the bug

When using the `unstyled` prop on Mantine components, variant classes are being applied when they shouldn't be. The variant styling still appears even when `unstyled={true}` is set, which defeats the purpose of the unstyled prop.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button variant="filled" unstyled>
      Click me
    </Button>
  );
}
```

### Expected behavior

When `unstyled={true}` is set, the component should not have any variant-specific classes applied. The button should render without the `filled` variant styles.

Currently, the variant classes are being added even with `unstyled={true}`, causing the component to still have variant styling when it should be completely unstyled.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
