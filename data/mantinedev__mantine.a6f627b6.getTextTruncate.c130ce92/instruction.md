# Bug Report

### Describe the bug

The `truncate` prop on the `Text` component is not working as expected. When I set `truncate="start"`, the text is being truncated at the end instead of the start. Similarly, when I set `truncate="end"`, it truncates at the start.

### Reproduction

```jsx
import { Text } from '@mantine/core';

// This should truncate at the start but truncates at the end
<Text truncate="start">
  This is a very long text that should be truncated at the beginning
</Text>

// This should truncate at the end but truncates at the start
<Text truncate="end">
  This is a very long text that should be truncated at the end
</Text>
```

### Expected behavior

- `truncate="start"` should add ellipsis at the beginning of the text (e.g., "...ng text")
- `truncate="end"` should add ellipsis at the end of the text (e.g., "This is a very lon...")

Currently, the behavior is reversed - `truncate="start"` acts like `truncate="end"` and vice versa.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
