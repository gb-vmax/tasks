# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the parser seems to fail when processing ESM import/export statements. The markdown-to-AST conversion is not working correctly and appears to be related to how exit handlers are structured.

### Reproduction

```js
const mdx = `
import { Component } from './Component'

# Hello World

<Component />
`

// Attempting to parse this MDX content
const result = compile(mdx)
// Parser fails to properly handle the mdxjsEsm exit events
```

### Expected behavior

The MDX parser should correctly handle ESM import/export statements and generate the appropriate AST nodes. Exit handlers for `mdxjsEsm` and `mdxjsEsmData` should be called properly during the parsing process.

### Additional context

This seems to affect any MDX document that includes import or export statements at the top level. The issue appears to be in the `mdxjsEsmFromMarkdown()` function where exit handlers are configured.

---
Repository: /testbed
