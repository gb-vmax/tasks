# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where tokenization appears to be happening in the wrong order. When parsing MDX content, the tokenizer seems to be receiving its arguments in an incorrect sequence, which causes unexpected parsing behavior.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document with **bold text**.
`

const result = await compile(mdxContent)
// Parser produces unexpected output or fails to correctly tokenize content
```

### Expected behavior

The MDX content should be parsed correctly with proper tokenization. The parser should process the markdown elements (headings, bold text, etc.) in the correct order and produce valid output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The tokenizer creation logic might have an issue with how it's passing parameters around.

---
Repository: /testbed
