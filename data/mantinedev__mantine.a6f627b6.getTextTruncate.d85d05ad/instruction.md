# Bug Report

### Describe the bug

The `truncate` prop on the `Text` component is not working as expected. When I set `truncate="start"` or `truncate={true}`, the text truncation doesn't apply correctly. It seems like the truncation behavior is inverted or broken.

### Reproduction

```jsx
import { Text } from '@mantine/core';

// This should truncate at the start but doesn't work
<Text truncate="start">
  This is a very long text that should be truncated at the start with ellipsis
</Text>

// This should truncate (default to end) but also doesn't work
<Text truncate>
  This is a very long text that should be truncated with ellipsis
</Text>
```

### Expected behavior

- When `truncate="start"` is set, text should be truncated at the beginning with ellipsis (e.g., "...end of text")
- When `truncate={true}` is set, text should be truncated at the end with ellipsis (e.g., "beginning of text...")
- When `truncate="end"` is set, text should be truncated at the end with ellipsis

Currently none of these seem to work properly. The text either doesn't truncate at all or truncates in the wrong direction.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
