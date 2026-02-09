# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where flow content is not being processed correctly. It appears that the parser is not properly handling flow-level constructs in MDX documents, which is causing certain markdown elements to fail parsing or render incorrectly.

### Reproduction

```js
const mdx = `
# Heading

This is a paragraph.

- List item 1
- List item 2

Another paragraph here.
`

// Parse the MDX content
const result = compile(mdx)
// Flow constructs are not being recognized properly
```

When trying to parse MDX documents with standard flow-level markdown constructs (headings, paragraphs, lists, etc.), the parser seems to be using the wrong construct configuration internally.

### Expected behavior

The parser should correctly process all flow-level markdown constructs and generate the appropriate output. Flow content should be tokenized using the proper flow constructs configuration.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
