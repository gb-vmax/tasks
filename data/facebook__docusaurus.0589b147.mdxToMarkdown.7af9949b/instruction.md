# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX markdown serialization. When trying to convert MDX AST back to markdown format, the output seems to be missing the expression syntax completely. The MDX expressions just disappear from the serialized output.

### Reproduction

```js
import {toMarkdown} from 'mdast-util-to-markdown'
import {mdxToMarkdown} from 'remark-mdx'

const mdxAst = {
  type: 'root',
  children: [
    {
      type: 'mdxFlowExpression',
      value: 'someExpression',
      data: {estree: {...}}
    }
  ]
}

const result = toMarkdown(mdxAst, {
  extensions: [mdxToMarkdown()]
})

// Expected: {someExpression}
// Actual: (empty or missing the expression)
```

### Expected behavior

MDX expressions should be properly serialized back to their original syntax when converting from AST to markdown. All three extension types (expressions, JSX, and ESM) should be included in the output.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
