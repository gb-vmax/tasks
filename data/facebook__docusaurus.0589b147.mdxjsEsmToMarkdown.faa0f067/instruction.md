# Bug Report

### Describe the bug
When trying to serialize MDX content that contains ESM imports/exports, the output is broken and the handlers don't seem to be applied correctly. The MDX content with ESM blocks doesn't get properly converted back to markdown format.

### Reproduction
```js
import { toMarkdown } from 'mdast-util-to-markdown'
import { mdxjsEsmToMarkdown } from 'remark-mdx'

const tree = {
  type: 'root',
  children: [
    {
      type: 'mdxjsEsm',
      value: 'import Foo from "./foo"'
    }
  ]
}

const result = toMarkdown(tree, {
  extensions: [mdxjsEsmToMarkdown()]
})

console.log(result)
// Expected: import Foo from "./foo"
// Actual: [object Object] or empty/malformed output
```

### Expected behavior
The MDX ESM blocks should be properly serialized back to their original import/export statements when converting the AST to markdown.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently, as the same code was working before. Any help would be appreciated!

---
Repository: /testbed
