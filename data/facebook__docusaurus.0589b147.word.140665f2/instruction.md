# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where `import` and `export` statements are not being recognized correctly. It seems like the parser is failing to properly detect these keywords at the beginning of lines.

### Reproduction

```mdx
import { Component } from './component'

export const meta = { title: 'Test' }

# Hello World
```

When trying to parse this MDX content, the import and export statements are not being processed as expected. The parser appears to be treating them as regular text instead of ESM statements.

### Expected behavior

The parser should correctly identify `import` and `export` keywords and process them as ESM statements, allowing proper module imports and exports in MDX files.

### Additional context

This seems to affect any MDX file that uses standard ES6 import/export syntax. The issue prevents components and metadata from being properly imported/exported in MDX documents.

---
Repository: /testbed
