# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the markdown-to-AST conversion seems to be broken. When trying to parse MDX content, I'm getting unexpected behavior and the output doesn't match what I'd expect from the remark-mdx plugin.

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

<Component prop="value" />
`

const result = processor.processSync(mdxContent)
console.log(result)
```

The processing fails or produces incorrect output. It seems like the plugin extensions aren't being registered properly.

### Expected behavior

The MDX content should be parsed correctly with JSX elements being recognized and converted to the appropriate AST nodes. The plugin should register its extensions to both the micromark parser and the fromMarkdown/toMarkdown handlers.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This might be related to how the plugin registers its extensions internally. The parsing pipeline doesn't seem to be set up correctly.

---
Repository: /testbed
