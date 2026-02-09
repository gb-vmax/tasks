# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where import statements are being handled incorrectly. It seems like the parser is either skipping imports or processing them when it shouldn't be, leading to unexpected behavior in my MDX files.

### Reproduction

```mdx
import { Component } from './component'

# Hello World

Some content here
```

When parsing this MDX file, the import statement doesn't seem to be processed correctly. The behavior appears inconsistent - sometimes imports are recognized, sometimes they're not.

### Expected behavior

Import declarations at the top of MDX files should be consistently parsed and handled properly regardless of the parsing context.

### Additional context

This seems to have started happening recently. I'm using remark-mdx for parsing MDX content and the imports are critical for my component usage. The issue appears to be related to how the parser validates import statements during tokenization.

---
Repository: /testbed
