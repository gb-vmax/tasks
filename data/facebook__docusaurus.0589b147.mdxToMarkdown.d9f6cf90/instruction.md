# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression serialization where expressions are not being properly converted back to markdown format. It seems like expressions that should be preserved are getting mangled or lost during the markdown generation process.

### Reproduction

```js
import { mdxToMarkdown } from 'remark-mdx';

const tree = {
  type: 'root',
  children: [
    {
      type: 'mdxJsxFlowElement',
      name: 'Component',
      children: []
    },
    {
      type: 'mdxFlowExpression',
      value: 'someExpression'
    }
  ]
};

const result = toMarkdown(tree, { extensions: [mdxToMarkdown()] });
// Expression output is incorrect or missing
```

When converting an MDX AST back to markdown, JSX elements work fine but expressions don't serialize correctly. The output either duplicates expressions or doesn't handle them in the right order.

### Expected behavior

MDX expressions should be properly serialized to their original markdown representation when using `mdxToMarkdown()`. The conversion should maintain the correct structure and order of all MDX elements including expressions, JSX, and ESM imports.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
