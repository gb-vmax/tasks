# Bug Report

### Describe the bug

I'm experiencing an issue with MDX markdown serialization after a recent update. When I try to serialize MDX content back to markdown (using `toMarkdown`), it seems to be using the wrong extensions configuration. The output is completely broken and doesn't match the expected markdown format.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkMdx from 'remark-mdx'
import remarkStringify from 'remark-stringify'

const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(remarkStringify)

const mdxContent = `
# Hello

<MyComponent prop="value" />

Some text here.
`

const ast = processor.parse(mdxContent)
const output = processor.stringify(ast)

console.log(output)
// Expected: proper MDX markdown
// Actual: malformed output or error
```

### Expected behavior

The MDX content should be properly serialized back to markdown format with JSX components intact. The `toMarkdown` extensions should be applied correctly to handle MDX-specific syntax.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after updating to the latest version. The serialization was working fine before.

---
Repository: /testbed
