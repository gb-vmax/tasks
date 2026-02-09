# Bug Report

### Describe the bug

The `Highlight` component is behaving incorrectly - it's highlighting the entire text even when a specific highlight string is provided, instead of only highlighting the matching portions.

### Reproduction

```jsx
import { Highlight } from '@mantine/core';

// This highlights the entire text instead of just "world"
<Highlight highlight="world">
  Hello world, this is a test
</Highlight>

// Expected: Only "world" should be highlighted
// Actual: The entire string "Hello world, this is a test" is highlighted
```

When passing a highlight prop with a search term, the component highlights everything rather than just the matching text. This makes the component unusable for its intended purpose of emphasizing specific parts of text.

### Expected behavior

Only the text matching the `highlight` prop should be highlighted, not the entire string. In the example above, only the word "world" should be marked as highlighted.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
