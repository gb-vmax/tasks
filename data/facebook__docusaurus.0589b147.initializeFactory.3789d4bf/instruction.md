# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be skipping or incorrectly processing certain content. After some investigation, it appears that the tokenizer is not properly handling data sequences and construct matching.

### Reproduction

When parsing MDX content with specific patterns, the output is incomplete or malformed. Here's a minimal example:

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

Some text with **bold** content.

More paragraphs here.
`

const result = await compile(mdxContent)
// Expected: Full content parsed correctly
// Actual: Some content is missing or incorrectly tokenized
```

### Expected behavior

The MDX compiler should correctly parse and tokenize all content, including nested constructs and data sequences. All text nodes should be properly closed before transitioning to other tokens.

### Additional context

This seems to affect content parsing in general, particularly when transitioning between different token types. The issue manifests as either missing content in the output or unexpected parsing behavior.

---
Repository: /testbed
