# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data parsing where the content seems to be getting corrupted or not processed correctly. When using ESM imports/exports in MDX files, the parser appears to be handling the data in the wrong order, leading to malformed or missing content in the output.

### Reproduction

```mdx
import { Component } from './component'

export const metadata = {
  title: 'My Page'
}

# Hello World

<Component />
```

When this MDX file is processed, the ESM block data doesn't get parsed correctly. The import/export statements either don't appear in the output or are malformed.

### Expected behavior

The ESM imports and exports should be properly extracted and preserved during parsing. The `exitMdxjsEsmData` handler should process the token data in the correct sequence so that the ESM content is accurately represented in the AST.

### System Info

- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
