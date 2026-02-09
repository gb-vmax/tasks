# Bug Report

### Describe the bug

The RingProgress component is rendering incorrectly after a recent update. The rings appear to have wrong sizing and the progress segments are inverted - the filled portion and empty portion seem to be swapped.

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
        { value: 25, color: 'orange' }
      ]}
    />
  );
}
```

### Expected behavior

- The ring should display with proper thickness relative to its size
- The colored sections should represent the filled portions (40% cyan, 25% orange)
- The remaining portion should be empty/background

### Actual behavior

- The ring thickness appears incorrect (too thick or overlapping)
- The progress sections appear inverted - what should be filled shows as empty and vice versa

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
