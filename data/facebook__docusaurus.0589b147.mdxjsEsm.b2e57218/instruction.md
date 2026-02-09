# Bug Report

### Describe the bug

I'm experiencing an issue with MDX import/export statement parsing. It seems like the parser is not correctly recognizing import and export statements in my MDX files. The statements appear to be skipped or ignored during processing.

### Reproduction

When I have an MDX file with standard import/export statements like:

```mdx
import { Component } from './component'

export const metadata = { title: 'Example' }

# My Content
```

The imports and exports are not being parsed correctly. It looks like the parser is expecting something different after the `import` or `export` keyword.

Additionally, I noticed that when there are multiple statements in the ESTree body, some of them seem to be getting skipped during iteration. The processing appears to be off by one element.

### Expected behavior

Import and export statements should be recognized and parsed correctly when followed by a space (character code 32). The parser should properly iterate through all nodes in the ESTree body without skipping any elements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
