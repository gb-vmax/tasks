# Bug Report

### Describe the bug

The Highlight component is not working correctly when trying to highlight text that contains special regex characters. When the text to be highlighted includes characters like parentheses, the highlighting fails or produces unexpected results.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This doesn't highlight correctly
<Highlight highlight="test()" >
  Some text with test() in it
</Highlight>

// Also fails with other special characters
<Highlight highlight="price: $50">
  The price: $50 is correct
</Highlight>
```

### Expected behavior

The component should properly escape special regex characters and highlight the exact text provided in the `highlight` prop, regardless of whether it contains special characters like `()`, `^`, `$`, etc.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
