# Bug Report

### Describe the bug

I'm encountering a parsing issue when using MDX with import/export statements. It appears that when there are defined module specifiers, the parser fails to process subsequent code in the ESM block correctly.

### Reproduction

```mdx
import { something } from 'module';

export const config = {
  value: 'test'
};

Some content here...
```

When parsing MDX files with both import and export statements, especially when module specifiers are defined, the content after the import/export block doesn't get processed properly. The parser seems to stop mid-way through handling the ESM body.

### Expected behavior

The parser should correctly handle all import/export statements and continue processing the rest of the MDX content without issues. All module specifiers should be properly tracked and the entire ESM block should be parsed successfully.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
