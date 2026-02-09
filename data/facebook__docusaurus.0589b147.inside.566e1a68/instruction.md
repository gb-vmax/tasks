# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX ESM blocks that contain line endings. It seems like the parser is not correctly handling multi-line ESM import/export statements in MDX files.

### Reproduction

```mdx
import { something } from 'somewhere'
import { anotherThing } from 'another-place'

# My Content

Some text here
```

When parsing MDX files with multiple import statements on separate lines, the parser appears to exit the ESM data state prematurely. This causes the subsequent lines to be incorrectly parsed or the entire ESM block to not be recognized properly.

### Expected behavior

Multi-line ESM import/export blocks should be parsed correctly as a single ESM node. The parser should continue consuming the ESM data until it reaches the actual end of the ESM block, not exit early when encountering line endings within the block.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
