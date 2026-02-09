# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in MDX files. After a recent update, the TOC export seems to be broken and references to imported TOC slices are not working correctly.

### Reproduction

When using TOC slices in an MDX file with imports:

```mdx
import TOCSlice from './toc-slice.mdx';

# My Document

<TOCSlice />
```

The generated TOC export references the wrong property name for the imported slice, causing the TOC to fail rendering or show undefined values.

### Expected behavior

The TOC should correctly reference imported slices using their `importName` property and generate valid JavaScript that can be executed without errors. The spread elements in the TOC array should properly expand the imported slice content.

### System Info
- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

---
Repository: /testbed
