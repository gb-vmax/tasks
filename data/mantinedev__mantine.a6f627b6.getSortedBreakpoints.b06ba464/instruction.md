# Bug Report

### Describe the bug

I'm experiencing an issue with breakpoint sorting in Mantine components. It appears that breakpoints are being sorted in the wrong order (descending instead of ascending), which is causing responsive layouts to behave incorrectly.

### Reproduction

```tsx
import { Group } from '@mantine/core';

// Using breakpoints in a component
<Group
  breakpoints={['xs', 'sm', 'md', 'lg', 'xl']}
>
  {/* content */}
</Group>
```

When the component renders, the breakpoints seem to be applied in reverse order. Styles that should apply at smaller breakpoints are being applied at larger ones instead.

### Expected behavior

Breakpoints should be sorted in ascending order (from smallest to largest) so that media queries and responsive styles are applied correctly. The smallest breakpoint should have the lowest priority and the largest breakpoint should have the highest priority.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
