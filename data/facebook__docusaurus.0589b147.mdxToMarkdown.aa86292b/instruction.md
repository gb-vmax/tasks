# Bug Report

### Describe the bug

After a recent update, MDX serialization is producing incorrect output. When converting MDX AST back to markdown, JSX elements are not being properly serialized - they're either missing from the output or appearing in the wrong format.

### Reproduction

```js
import { toMarkdown } from 'mdast-util-to-markdown'
import { mdxToMarkdown } from 'remark-mdx'

const mdxAst = {
  type: 'root',
  children: [
    {
      type: 'mdxJsxFlowElement',
      name: 'Component',
      attributes: [],
      children: []
    }
  ]
}

const result = toMarkdown(mdxAst, {
  extensions: [mdxToMarkdown()]
})

console.log(result)
// Expected: <Component />
// Actual: (empty or malformed output)
```

### Expected behavior

JSX elements should be correctly serialized when converting MDX AST to markdown string. The output should preserve JSX syntax like `<Component />` or `<div>content</div>`.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
