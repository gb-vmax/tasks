# Bug Report

### Describe the bug

When processing MDX files with `format: "md"`, the remarkMdx plugin is being applied when it shouldn't be. This causes markdown files to be incorrectly parsed as MDX, leading to unexpected behavior when processing standard markdown syntax.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const markdown = `
# Hello World

This is a regular markdown file.
`

const result = await compile(markdown, {
  format: 'md'
})

// The markdown is being processed with MDX syntax rules
// instead of being treated as plain markdown
```

### Expected behavior

When `format` is set to `"md"`, the processor should treat the content as plain markdown and not apply MDX-specific transformations. The remarkMdx plugin should only be used when the format is NOT "md" (i.e., when it's "mdx" or other MDX formats).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
