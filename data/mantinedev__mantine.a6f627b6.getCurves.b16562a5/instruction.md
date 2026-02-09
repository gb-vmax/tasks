# Bug Report

### Describe the bug

The RingProgress component is rendering segments in the wrong order/position. The segments appear to start from an incorrect offset position and the visual rendering doesn't match the expected layout.

### Reproduction

```tsx
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

When rendering the above component, the segments don't align properly. The first segment starts at an unexpected position instead of the top, and subsequent segments are offset incorrectly.

### Expected behavior

The ring segments should start from the top (12 o'clock position) and progress clockwise with each segment positioned immediately after the previous one, without gaps or overlaps.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: Any

---
Repository: /testbed
