# Bug Report

### Describe the bug

After a recent update, export declarations in MDX files are not being parsed correctly. The parser seems to be creating malformed AST nodes for export statements, which causes issues when trying to process or transform MDX content.

### Reproduction

```js
const mdx = `
export const foo = 'bar'

# Hello World
`

// Parse the MDX content
const result = compile(mdx)
// The export declaration node in the AST is incorrect
```

When parsing MDX files with export statements, the resulting AST nodes don't have the expected structure. The declaration information appears to be missing or attached to the wrong node.

### Expected behavior

Export declarations should be parsed into properly structured AST nodes with all declaration information correctly attached. The parser should maintain the relationship between the export statement and its declaration.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
