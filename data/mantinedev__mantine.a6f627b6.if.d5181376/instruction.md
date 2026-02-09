# Bug Report

### Describe the bug

When using the `Highlight` component with `null` or `undefined` highlight prop, the component doesn't display the original text anymore. The text completely disappears instead of showing the unhighlighted version.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This renders nothing instead of showing "Hello World"
<Highlight highlight={null}>Hello World</Highlight>

// Same issue with undefined
<Highlight highlight={undefined}>Hello World</Highlight>
```

### Expected behavior

When the highlight prop is `null` or `undefined`, the component should display the original text without any highlighting applied. The text should still be visible to the user.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
