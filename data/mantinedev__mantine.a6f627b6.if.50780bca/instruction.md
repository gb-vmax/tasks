# Bug Report

### Describe the bug

When using the `Highlight` component without providing a highlight prop (or with `null`/`undefined`), the entire text is being highlighted instead of showing the plain text without any highlighting.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This incorrectly highlights the entire text
<Highlight highlight={null}>Hello World</Highlight>

// Same issue with undefined
<Highlight highlight={undefined}>Hello World</Highlight>
```

### Expected behavior

When no highlight value is provided (null, undefined, or empty), the text should be displayed normally without any highlighting applied. The component should treat it as if there's nothing to highlight.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
