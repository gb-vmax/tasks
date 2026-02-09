# Bug Report

### Describe the bug

The `Text` component's `truncate` prop is not working correctly. When I set `truncate="start"`, the text gets truncated from the end instead of the start. Also, when using `truncate={true}`, the text doesn't truncate at all.

### Reproduction

```jsx
import { Text } from '@mantine/core';

// This should truncate from the start but truncates from the end
<Text truncate="start">
  This is a very long text that should be truncated from the beginning
</Text>

// This should truncate from the end but doesn't truncate at all
<Text truncate={true}>
  This is a very long text that should be truncated from the end
</Text>
```

### Expected behavior

- When `truncate="start"` is set, text should be truncated from the beginning (e.g., "...end of text")
- When `truncate="end"` is set, text should be truncated from the end (e.g., "beginning of text...")
- When `truncate={true}` is set, text should default to truncating from the end

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
