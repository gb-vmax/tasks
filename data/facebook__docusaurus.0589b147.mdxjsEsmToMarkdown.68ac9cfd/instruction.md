# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM export/import statements not being properly serialized back to markdown. When trying to convert an MDX AST back to markdown format, the ESM nodes seem to be causing problems or getting dropped entirely.

### Reproduction

```js
import { toMarkdown } from 'mdast-util-to-markdown'
import { mdxjsEsmToMarkdown } from '@mdx-js/mdx'

const tree = {
  type: 'root',
  children: [
    {
      type: 'mdxjsEsm',
      value: 'import { Button } from "./components"'
    }
  ]
}

const result = toMarkdown(tree, {
  extensions: [mdxjsEsmToMarkdown()]
})

// The import statement is not included in the output
console.log(result)
```

### Expected behavior

The MDX ESM import/export statements should be properly serialized and included in the markdown output. The conversion should preserve the original ESM syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
