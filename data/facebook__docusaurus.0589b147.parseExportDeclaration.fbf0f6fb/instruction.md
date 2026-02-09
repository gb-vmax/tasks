# Bug Report

### Describe the bug

I'm encountering an issue with export declarations in MDX files. When parsing export statements, the parser seems to be losing context information, which causes problems with certain export patterns.

### Reproduction

```js
// In an MDX file
export const myVariable = 'test value'

export function myFunction() {
  return 'result'
}
```

When these exports are parsed, they don't maintain the proper node context. This leads to incorrect AST generation for export declarations.

### Expected behavior

Export declarations should properly preserve their node information during parsing. The parser should maintain the export node context throughout the statement parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
