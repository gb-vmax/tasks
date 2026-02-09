# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where fragments are not being properly created. When processing MDX content, the compiler seems to generate invalid AST nodes with empty type fields and null children arrays instead of proper fragment nodes.

### Reproduction

```jsx
import {compile} from '@mdx-js/mdx'

const mdx = `
# Hello

Some content here

<Component>
  Nested content
</Component>
`

const result = await compile(mdx)
```

When the above code runs, the internal AST structure appears to be malformed. The compiler should be creating proper fragment nodes during the buffering phase, but instead creates nodes with empty types and null children.

### Expected behavior

The compiler should generate valid fragment nodes with:
- `type: "fragment"`
- `children: []` (empty array, not null)

This affects any MDX content that requires fragment handling during compilation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
