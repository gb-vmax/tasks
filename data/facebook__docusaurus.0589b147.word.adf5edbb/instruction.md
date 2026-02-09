# Bug Report

### Describe the bug

MDX import/export statements are not being recognized correctly. When trying to use standard ES module syntax in MDX files, the parser fails to detect valid import and export declarations.

### Reproduction

```mdx
import Component from './Component'

export const metadata = { title: 'Example' }

# My Content
```

The parser doesn't recognize these as valid import/export statements and they're not processed correctly.

### Expected behavior

Standard ES module import and export statements should be properly detected and parsed in MDX files. The syntax above should work as expected.

### Additional context

This seems to affect basic MDX functionality where imports and exports are essential for component composition and metadata. The issue appears to be related to how the parser identifies these keywords.

---
Repository: /testbed
