# Bug Report

### Describe the bug

The `Highlight` component is not properly escaping special regex characters in the search term, causing the highlighting to fail when the search string contains characters like `*`, `+`, `?`, `.`, etc. These characters are being treated as regex operators instead of literal characters.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This doesn't work correctly - the asterisk is treated as a regex quantifier
<Highlight highlight="test*">
  This is a test* string that should be highlighted
</Highlight>

// Similarly with other special characters
<Highlight highlight="price: $10.99">
  The price: $10.99 should be highlighted
</Highlight>
```

### Expected behavior

Special regex characters in the highlight string should be treated as literal characters and properly highlighted in the text. For example, searching for "test*" should match the literal string "test*" and not be interpreted as a regex pattern.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
