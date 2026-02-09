# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain valid markdown constructs are being incorrectly rejected or causing the parser to enter an invalid state. It seems like the tokenizer is skipping valid constructs when it should be trying them.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`

const result = await compile(mdxContent)
// Parser fails or produces unexpected output
```

### Expected behavior

The MDX content should parse correctly and all markdown constructs should be recognized. The tokenizer should attempt all available constructs before giving up.

### Additional context

This appears to be related to how the tokenizer handles construct validation. When one construct fails, it should properly restore state and try the next available construct, but instead it seems to be skipping constructs or not attempting all of them.

---
Repository: /testbed
