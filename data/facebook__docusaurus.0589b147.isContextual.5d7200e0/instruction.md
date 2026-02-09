# Bug Report

### Describe the bug

I'm encountering an issue where contextual keywords in MDX are not being recognized correctly. It seems like the parser is failing to identify contextual keywords (like `async`, `from`, `of`, etc.) in certain scenarios, which is causing syntax errors or unexpected parsing behavior.

### Reproduction

When trying to parse MDX content that uses contextual keywords, the parser doesn't properly identify them. For example:

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
export async function getData() {
  return { data: 'test' }
}
`

// Parser fails to recognize 'async' as a contextual keyword
const result = await compile(mdxContent)
```

This also affects other contextual keywords in various contexts, particularly in export statements and function declarations.

### Expected behavior

The parser should correctly identify and handle contextual keywords. These keywords should be recognized based on their context in the code, allowing valid JavaScript/MDX syntax to parse without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
