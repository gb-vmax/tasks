# Bug Report

### Describe the bug

The `Highlight` component is not working properly when highlighting text that contains special regex characters. When I try to highlight strings with characters like `$`, `^`, `|`, etc., the highlighting either doesn't work at all or produces unexpected results.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This doesn't highlight correctly
<Highlight highlight="$100">
  The price is $100 for this item
</Highlight>

// Also fails with other special characters
<Highlight highlight="test^2">
  The formula is test^2
</Highlight>
```

### Expected behavior

The component should correctly highlight text containing special regex characters like `$`, `^`, `|`, `#`, etc. The special characters should be treated as literal characters to match, not as regex operators.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
