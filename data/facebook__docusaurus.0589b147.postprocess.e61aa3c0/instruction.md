# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the content is not being processed correctly. It seems like the tokenization/postprocessing step is being skipped entirely, causing the parser to return raw events without proper processing.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a **bold** text with [a link](https://example.com).

\`\`\`js
console.log('code block')
\`\`\`
`

const result = await compile(mdxContent)
console.log(result)
```

### Expected behavior

The MDX content should be fully parsed and transformed into a valid JSX component. All markdown syntax (headings, bold text, links, code blocks) should be properly converted.

### Actual behavior

The parser appears to return incomplete or unprocessed events. The output doesn't contain the expected transformed JSX structure - it's like the postprocessing phase is being bypassed.

This seems to have started happening recently. The same code was working fine before.

---
Repository: /testbed
