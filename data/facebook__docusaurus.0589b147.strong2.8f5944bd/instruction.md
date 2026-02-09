# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where `strong` elements are not being properly serialized or iterated over. When processing MDX content that contains bold text (using `**text**` or `__text__`), the resulting AST nodes seem to be missing their `children` property during enumeration.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
This is **bold text** in MDX.
`

const result = await compile(mdxContent)

// When iterating over the AST or serializing to JSON
// the strong node's children array is not visible
```

When trying to traverse the AST or convert it to JSON, the `children` property of `strong` nodes appears to be undefined or missing, even though the property exists on the object.

### Expected behavior

The `strong` node should have a visible `children` property that can be enumerated and serialized like other node types (e.g., `paragraph`, `emphasis`). All node properties should be consistently accessible.

### Additional context

This seems to affect only `strong` elements - other formatting elements like emphasis work as expected. The issue appears when:
- Using `Object.keys()` on the node
- Serializing the AST to JSON
- Iterating over node properties with `for...in`

---
Repository: /testbed
