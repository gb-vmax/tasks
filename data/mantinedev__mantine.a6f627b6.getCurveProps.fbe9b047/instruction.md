# Bug Report

### Describe the bug

The RingProgress component is rendering incorrectly with wrong dimensions and progress visualization. The ring appears too large and the progress percentage doesn't match the actual visual representation.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      size={120}
      thickness={12}
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
      ]}
    />
  );
}
```

When rendered, the ring progress shows incorrect sizing - the radius calculation seems off and the progress arcs don't align with the expected percentage values. For example, a 40% section appears to take up roughly 80% of the circle.

### Expected behavior

The RingProgress component should:
- Calculate the correct radius based on size and thickness
- Display progress sections that accurately represent their percentage values
- Maintain proper spacing between the ring and the container edges

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
