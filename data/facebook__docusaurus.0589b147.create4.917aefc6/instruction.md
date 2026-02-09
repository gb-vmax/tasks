# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where tokenization seems to be broken. When parsing MDX content, the parser is not correctly handling the token creation flow, which results in incorrect parsing behavior.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test paragraph with **bold text**.
`

const result = await compile(mdxContent)
// Parser fails to correctly tokenize the content
```

### Expected behavior

The MDX content should be parsed correctly with proper tokenization of all elements (headings, paragraphs, bold text, etc.). The tokenizer should receive the correct arguments in the proper order to process the content stream.

### Additional context

This appears to affect the core parsing functionality. The issue manifests when the parser tries to create tokenizers for processing text content. It seems like there might be an issue with how arguments are being passed to the tokenizer creation function.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
