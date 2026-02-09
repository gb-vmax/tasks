# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where import/export statements are not being recognized correctly. It seems like the parser is failing to properly detect these statements when they should be valid.

### Reproduction

When trying to use standard import or export statements in an MDX file, they're not being parsed as expected. For example:

```mdx
import { Component } from './Component'

export const metadata = { title: 'Example' }

# My Content
```

The parser appears to be having trouble identifying the import/export keywords, which causes the entire MDX processing to fail or behave unexpectedly.

### Expected behavior

Import and export statements should be properly recognized and parsed in MDX files. The parser should correctly identify these keywords followed by a space and process them accordingly.

### Additional context

This seems to affect both import and export statements at the beginning of MDX files. The issue might be related to how the parser checks for whitespace after the keywords.

---
Repository: /testbed
