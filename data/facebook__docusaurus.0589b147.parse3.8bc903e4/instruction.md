# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be initializing incorrectly. After a recent update, documents that previously parsed correctly are now failing or producing unexpected results.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document with some content.
`

const result = await compile(mdxContent)
// Parser fails or produces incorrect output
```

### Expected behavior

The MDX content should parse successfully and generate the correct output. The parser should properly initialize its tokenizer with the appropriate constructs and initial state.

### Additional context

This seems to affect basic MDX documents. The parsing behavior changed after updating to a newer version, and documents that worked before are no longer processing correctly. It appears related to how the parser initializes its internal tokenizer components.

---
Repository: /testbed
