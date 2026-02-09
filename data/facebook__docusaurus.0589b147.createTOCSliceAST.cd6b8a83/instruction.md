# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in MDX files. After a recent update, the TOC export seems to be malformed and is causing runtime errors when trying to render pages with imported TOC slices.

### Reproduction

1. Create an MDX file that uses TOC slices with imports
2. Import a TOC slice from another file
3. Try to render the page

The generated TOC export appears to have an incorrect structure. When inspecting the compiled output, the spread elements in the TOC array are not being created properly.

Example setup:
```mdx
---
toc_slice: true
---

# My Document

## Section 1
Content here...

## Section 2
More content...
```

Then importing in another file:
```mdx
import TOCSlice from './other-doc.mdx';

# Main Document
```

### Expected behavior

The TOC should be properly exported and the spread elements should reference the correct import names. The page should render without errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

The issue seems related to how the AST nodes are being constructed for TOC slices. The spread element structure might not be matching what the runtime expects.

---
Repository: /testbed
