# Bug Report

### Describe the bug

The Highlight component is not working correctly when trying to highlight text that contains special regex characters like backslashes. The highlighting fails and the text appears without any highlighting applied.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This doesn't highlight correctly
<Highlight highlight="test\value">
  Some text with test\value in it
</Highlight>

// Also fails with other special characters
<Highlight highlight="test*value">
  Some text with test*value in it
</Highlight>
```

When the highlight prop contains special regex characters (especially backslashes), the component doesn't properly highlight the matching text. The text renders but without any highlight styling applied.

### Expected behavior

The Highlight component should correctly highlight text even when the search term contains special regex characters like `\`, `*`, `+`, etc. These characters should be properly escaped so they're treated as literal characters rather than regex operators.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
