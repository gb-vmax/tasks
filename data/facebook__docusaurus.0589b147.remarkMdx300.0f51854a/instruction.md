# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the remark-mdx plugin doesn't seem to be processing MDX content correctly. The parser appears to be misconfigured internally, causing MDX-specific syntax (like JSX components) to not be recognized or transformed properly.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkMdx from 'remark-mdx'

const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)

const mdxContent = `
# Hello

<CustomComponent prop="value" />

Some text here.
`

const result = processor.processSync(mdxContent)
console.log(result)
```

When running this code, the MDX elements are not being parsed correctly. It seems like the micromark extensions aren't being applied properly during the parsing phase.

### Expected behavior

The MDX content should be properly parsed with JSX components recognized and transformed into the appropriate AST nodes. The micromark and fromMarkdown extensions should be correctly registered and applied during processing.

### System Info

- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently, possibly related to how the plugin registers its extensions internally. Any help would be appreciated!

---
Repository: /testbed
