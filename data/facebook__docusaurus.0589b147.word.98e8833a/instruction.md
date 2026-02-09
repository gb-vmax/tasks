# Bug Report

### Describe the bug

I'm experiencing an issue with MDX import/export statement parsing. It appears that import and export statements at the beginning of MDX files are no longer being recognized correctly. The parser seems to be failing to detect these statements, which causes the entire MDX processing to break.

### Reproduction

Create an MDX file with a simple import or export statement:

```mdx
import { Component } from './Component'

# Hello World

Some content here.
```

Or with an export:

```mdx
export const metadata = { title: 'Test' }

# My Document

Content goes here.
```

### Expected behavior

The parser should correctly identify and process `import` and `export` statements at the start of MDX files. Both statements should be parsed as ESM data and allow the rest of the MDX content to render normally.

### Actual behavior

The import/export statements are not being recognized, and the MDX file fails to parse correctly. It seems like the parser is rejecting valid ESM syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
