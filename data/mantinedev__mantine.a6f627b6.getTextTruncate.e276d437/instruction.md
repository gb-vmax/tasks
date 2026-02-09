# Bug Report

### Describe the bug

The `truncate` prop on the `Text` component is not working as expected. When I set `truncate="start"`, the text is not being truncated from the start. Similarly, when I use `truncate="end"` or `truncate={true}`, the truncation behavior seems broken.

### Reproduction

```jsx
import { Text } from '@mantine/core';

// This should truncate from the start but doesn't work correctly
<Text truncate="start">
  This is a very long text that should be truncated from the beginning
</Text>

// This should truncate from the end but also doesn't work
<Text truncate="end">
  This is a very long text that should be truncated from the end
</Text>

// Using boolean value
<Text truncate={true}>
  This is a very long text that should be truncated
</Text>
```

### Expected behavior

- When `truncate="start"` is set, the text should be truncated from the beginning with ellipsis at the start
- When `truncate="end"` or `truncate={true}` is set, the text should be truncated from the end with ellipsis at the end
- The truncation should apply the correct CSS class based on the prop value

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
