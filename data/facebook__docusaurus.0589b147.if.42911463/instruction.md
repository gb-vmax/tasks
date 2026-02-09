# Bug Report

### Describe the bug

When using the MDX loader with table of contents (TOC) functionality, duplicate TOC slice imports are being added to the import declaration. This causes the same import to appear multiple times in the generated code, which can lead to naming conflicts and unexpected behavior.

### Reproduction

```js
// When processing MDX files with TOC
// The import statement ends up with duplicate specifiers:
import { toc, toc, toc } from '@theme/TOCInline';

// Instead of the expected:
import { toc } from '@theme/TOCInline';
```

Steps to reproduce:
1. Create an MDX file with multiple headings
2. Process the file with the MDX loader
3. Check the generated import statements for the TOC slice

The import keeps getting added even when it already exists in the import declaration.

### Expected behavior

The TOC slice import should only be added once to the import declaration. If the import already exists, it should be skipped to avoid duplicates.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
