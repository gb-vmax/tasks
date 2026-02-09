# Bug Report

### Describe the bug

After a recent update, MDX expressions are no longer being serialized correctly when converting back to markdown. It seems like the `mdxExpressionToMarkdown()` extension is missing from the serialization pipeline, causing expressions to either be dropped or not rendered properly in the output.

### Reproduction

```js
import { mdxToMarkdown } from 'remark-mdx';

const options = { /* ... */ };
const extensions = mdxToMarkdown(options);

// Try to serialize MDX content with expressions like {variable}
// The expressions are not included in the output
```

When converting MDX AST back to markdown string, any inline expressions (like `{someVariable}`) or expression containers are not being processed and appear to be missing from the final output.

### Expected behavior

MDX expressions should be properly serialized when using `mdxToMarkdown()`. The function should return all necessary extensions including the expression serializer to handle inline expressions and expression blocks correctly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
