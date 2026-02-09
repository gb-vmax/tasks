# Bug Report

### Describe the bug

The TOC (Table of Contents) export is generating incorrect AST structure for TOC slices. Instead of spreading the imported TOC slice object, the code is now wrapping it in an `ObjectExpression` with a `name` property, which breaks the expected TOC structure.

### Reproduction

When using MDX with TOC slices imported from other files:

```mdx
import PartialTOC from './partial-toc.md';

# My Document

<PartialTOC />
```

The generated TOC export should spread the imported TOC items directly into the array, but instead it creates objects with a `name` property pointing to the import.

Expected TOC structure:
```js
export const toc = [
  ...PartialTOC,
  { value: 'Heading', id: 'heading', level: 2 }
]
```

Actual TOC structure being generated:
```js
export const toc = [
  { name: PartialTOC },
  { value: 'Heading', id: 'heading', level: 2 }
]
```

### Expected behavior

TOC slices should be spread into the TOC array using `SpreadElement` so that imported TOC items are properly merged with the current document's TOC items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
