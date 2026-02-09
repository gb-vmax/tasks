# Bug Report

### Describe the bug

Variant class names are not being applied correctly to components. When setting a variant prop on a component, the CSS classes are either missing entirely or have incorrect naming, causing the component to not render with the expected variant styles.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <>
      <Button variant="filled">Filled Button</Button>
      <Button variant="outline">Outline Button</Button>
      <Button variant="subtle">Subtle Button</Button>
    </>
  );
}
```

Expected: Buttons should render with their respective variant styles (filled, outline, subtle)
Actual: Buttons are not getting the correct variant class names applied, resulting in missing or incorrect styles

### Additional context

This affects all components that use the variant system. The issue seems to be related to how variant class names are being generated and applied to elements. Also noticed that when `unstyled` prop is used, the behavior is completely inverted from what's expected.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
