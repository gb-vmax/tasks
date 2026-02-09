# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the first construct in a list seems to be getting skipped or not processed correctly. This appears to affect how certain MDX syntax elements are being recognized and parsed.

### Reproduction

When parsing MDX content with multiple syntax constructs, the first construct in the list is not being handled properly. This leads to unexpected parsing behavior where valid MDX syntax is either ignored or incorrectly processed.

Example scenario:
```js
// MDX content with multiple constructs
const mdxContent = `
<Component />
export const data = {}
import Something from './file'
`

// The first syntax construct is not being applied correctly
// causing parsing to fail or produce incorrect output
```

### Expected behavior

All syntax constructs should be processed in order, including the first one in the list. The parser should correctly handle all MDX elements regardless of their position in the construct array.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like it might be related to how the construct list is being iterated or how items are being added to the existing array. The issue manifests when there are multiple constructs that need to be applied during parsing.

---
Repository: /testbed
