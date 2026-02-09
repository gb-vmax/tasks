# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM export serialization. When trying to convert MDX documents back to markdown format, ESM import/export statements are not being properly handled during the serialization process.

### Reproduction

```js
import { toMarkdown } from 'mdast-util-to-markdown'
import { mdxjsEsmToMarkdown } from 'remark-mdx'

const tree = {
  type: 'root',
  children: [
    {
      type: 'mdxjsEsm',
      value: 'export const foo = "bar"'
    }
  ]
}

const result = toMarkdown(tree, {
  extensions: [mdxjsEsmToMarkdown()]
})

// Expected: export const foo = "bar"
// Actual: ESM block is not rendered or throws an error
console.log(result)
```

### Expected behavior

The MDX ESM blocks should be correctly serialized back to their original format when converting the AST to markdown. The `mdxjsEsmToMarkdown()` function should provide proper handlers for ESM nodes.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
