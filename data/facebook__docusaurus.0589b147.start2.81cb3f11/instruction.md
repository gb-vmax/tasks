# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain constructs are being incorrectly disabled. It seems like the parser is not properly checking whether a construct should be disabled, and as a result, valid MDX syntax is being rejected.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document with various MDX features.
`

const result = await compile(mdxContent, {
  // ... your config
})
```

When trying to parse MDX documents with certain constructs (like headings, emphasis, etc.), they're being incorrectly treated as disabled even though they're not in the disable list.

### Expected behavior

The parser should correctly identify which constructs are disabled by checking the disable list properly. Valid MDX syntax should parse without issues.

### Additional context

This seems to have started happening recently. The parser appears to be checking construct names against the wrong property or using an incorrect method to verify if a construct is disabled.

---
Repository: /testbed
