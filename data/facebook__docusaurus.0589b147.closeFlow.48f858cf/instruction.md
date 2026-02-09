# Bug Report

### Describe the bug

I'm experiencing an issue with MDX document parsing where the flow is not being closed properly. When processing MDX content with nested structures, the parser seems to hang or fail to complete the document processing correctly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Heading

Some content here

\`\`\`js
code block
\`\`\`

More content
`

const result = await compile(mdxContent)
```

When compiling MDX documents with code blocks or other flow content, the parser doesn't finish processing correctly. The issue appears to be related to how the flow state is being cleaned up internally.

### Expected behavior

The MDX compiler should successfully parse and compile documents with flow content (like code blocks, blockquotes, etc.) and properly close all flow states. The compilation should complete without hanging or producing incomplete output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
