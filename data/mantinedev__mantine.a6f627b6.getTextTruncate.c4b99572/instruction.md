# Bug Report

### Describe the bug

The `truncate` prop on the `Text` component is not working correctly when set to `true` (boolean). It seems like the text truncation behavior has changed and now only accepts string values 'start' or 'end', but passing `truncate={true}` doesn't apply any truncation anymore.

### Reproduction

```jsx
import { Text } from '@mantine/core';

// This used to work but now doesn't truncate
<Text truncate>
  This is a very long text that should be truncated with ellipsis but it's not being truncated anymore
</Text>

// This still works
<Text truncate="end">
  This is a very long text that should be truncated with ellipsis
</Text>
```

### Expected behavior

When `truncate` is set to `true`, the text should be truncated at the end with ellipsis, similar to when `truncate="end"` is used. According to the TypeScript types, `truncate` accepts `'end' | 'start' | boolean`, so passing `true` should work.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
