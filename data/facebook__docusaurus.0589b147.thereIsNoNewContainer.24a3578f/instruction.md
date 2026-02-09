# Bug Report

### Bug: Incorrect offset calculation in MDX parser affecting line start positions

I've encountered an issue with the MDX parser where line start offsets are being calculated incorrectly. This seems to affect how the parser tracks positions within the document, particularly when processing continuation lines.

### Reproduction

When parsing MDX content with multiple lines, the offset tracking appears to be off. Here's a minimal example:

```js
import {compile} from '@mdx-js/mdx'

const mdxContent = `
# Heading

Some paragraph text
that continues on multiple lines
and should track offsets correctly
`

const result = await compile(mdxContent)
```

The parser's internal offset tracking for line starts doesn't align with the actual character positions in the source document. This becomes noticeable when trying to map positions back to the original source or when using source maps.

### Expected behavior

The `lineStartOffset` should accurately reflect the current line's starting position in the document, using the correct offset from the parser state.

### Additional context

This affects position tracking throughout the parsing process, which could impact:
- Source map generation
- Error reporting with accurate line/column information
- Any tooling that relies on precise position data from the parser

---
Repository: /testbed
