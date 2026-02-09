# Bug Report

### Describe the bug

After a recent update, MDX serialization is broken when converting back to markdown. It seems like only expression syntax is being handled, but JSX components and ESM imports/exports are completely ignored during the serialization process.

### Reproduction

```js
import { mdxToMarkdown } from 'remark-mdx';

const mdxAst = {
  type: 'root',
  children: [
    {
      type: 'mdxJsxFlowElement',
      name: 'CustomComponent',
      attributes: [],
      children: []
    },
    {
      type: 'mdxjsEsm',
      value: 'import Foo from "bar"'
    }
  ]
};

const result = mdxToMarkdown();
// JSX and ESM nodes are not serialized correctly
```

### Expected behavior

The `mdxToMarkdown()` function should properly serialize all MDX node types including:
- MDX expressions
- JSX elements (both flow and text)
- ESM import/export statements

Currently it looks like only expressions are working, making it impossible to round-trip MDX documents that contain JSX components or imports.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
