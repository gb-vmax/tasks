# Bug Report

### Describe the bug

I'm experiencing a parsing issue with MDX content that appears to be related to the context stack initialization. When parsing certain MDX files, the parser seems to lose track of the proper context, leading to unexpected parsing errors or incorrect AST generation.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX file with some content.

<CustomComponent>
  Some nested content
</CustomComponent>
`

const result = await compile(mdxContent)
// Parser fails or produces incorrect output
```

### Expected behavior

The MDX content should parse correctly and generate a valid AST. The parser should maintain proper context throughout the parsing process, especially when dealing with JSX components and nested structures.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

### Additional context

This seems to happen specifically with files that have a mix of markdown and JSX components. Simpler MDX files without JSX components parse fine, but once you introduce custom components or more complex structures, the context tracking appears to break down.

---
Repository: /testbed
