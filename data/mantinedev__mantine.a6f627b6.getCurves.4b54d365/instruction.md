# Bug Report

### Describe the bug

The RingProgress component is rendering incorrectly when displaying multiple sections. The offset calculations seem off, causing the sections to not align properly with their actual percentage values.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
        { value: 15, color: 'grape' }
      ]}
    />
  );
}
```

When rendering this component, the visual representation of the sections doesn't match the percentage values provided. The sections appear to be scaled incorrectly relative to each other.

### Expected behavior

Each section should be rendered proportionally to its value. A section with value 40 should take up 40% of the visible ring (excluding the root/background), a section with value 25 should take up 25%, etc.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
