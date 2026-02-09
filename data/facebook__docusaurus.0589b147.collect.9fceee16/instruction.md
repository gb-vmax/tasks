# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the position information for collected tokens appears to be off by one. The stops array that tracks token positions seems to be recording incorrect offsets relative to the accumulated value string.

### Reproduction

When parsing MDX content with multiple tokens, the position stops are being recorded before the value is updated rather than after. This causes the offset calculations to be incorrect.

```js
// Example MDX content that triggers the issue
const mdxContent = `
import Component from './Component'

<Component prop="value" />
`

// After parsing, the stops array positions don't align correctly
// with the actual character positions in the collected value string
```

### Expected behavior

The stops array should contain accurate position offsets that correspond to the correct character indices in the accumulated value string. Each stop should reflect the position *after* the value has been updated with the current chunk.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
