# Bug Report

Title: Syntax error in mdxjs-esm tokenizer causing parsing failures

### Describe the bug
After a recent update, MDX files with import/export statements are failing to parse correctly. The parser seems to be cutting off in the middle of processing ESM syntax, leading to incomplete tokenization.

### Reproduction
```mdx
import { Component } from './Component'

export const metadata = {
  title: 'Example'
}

# Hello World

<Component />
```

When trying to parse this MDX content, the parser throws errors or produces incomplete AST nodes. The issue appears to be related to how the ESM tokenizer processes import/export declarations.

### Expected behavior
MDX files with standard import/export statements should parse successfully without errors. The tokenizer should properly handle the full ESM syntax and generate a complete AST.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
