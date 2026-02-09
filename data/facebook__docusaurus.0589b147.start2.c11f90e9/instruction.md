# Bug Report

### Describe the bug

After a recent update, markdown ATX headings (headings with `#` symbols) are not being parsed correctly. The heading content is not being recognized and the document structure appears broken.

### Reproduction

```js
const mdx = `
# Main Heading

Some content here

## Subheading

More content
`

// Parse the MDX content
const result = await compile(mdx)
// Headings are not properly tokenized
```

When I try to parse MDX content with ATX-style headings, the parser seems to fail or produce incorrect output. The headings aren't being recognized as heading elements.

### Expected behavior

ATX headings should be properly parsed and tokenized. The heading structure should be preserved in the output, with proper hierarchy for `#`, `##`, `###`, etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
