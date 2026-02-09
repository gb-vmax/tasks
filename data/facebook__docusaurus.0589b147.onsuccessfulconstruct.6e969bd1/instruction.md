# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where content is not being processed correctly. It seems like the tokenizer is silently failing to construct tokens, resulting in incomplete or missing output when parsing MDX documents.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a paragraph with **bold** text.

\`\`\`js
const x = 1;
\`\`\`
`

const result = await compile(mdxContent)
// Expected: Full compiled output with all elements
// Actual: Some or all content is missing from the output
```

### Expected behavior

The MDX compiler should properly tokenize and construct all elements in the document, including headings, paragraphs, formatted text, and code blocks. All content should be present in the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started recently. The tokenizer seems to be skipping certain constructs during parsing, leading to incomplete rendering of MDX content.

---
Repository: /testbed
