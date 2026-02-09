# Bug Report

### Describe the bug

I'm experiencing an issue where MDX JSX elements are not being serialized correctly. The markdown output appears to be truncated or malformed when converting MDX JSX nodes back to markdown format.

### Reproduction

```js
const mdxAst = {
  type: 'mdxJsxFlowElement',
  name: 'Component',
  attributes: [
    {
      type: 'mdxJsxAttribute',
      name: 'prop',
      value: 'value'
    }
  ],
  children: []
};

// Attempting to serialize this to markdown
const result = mdxJsxToMarkdown().handlers.mdxJsxFlowElement(mdxAst);
// Result is incomplete or throws an error
```

When trying to convert MDX JSX elements with attributes back to markdown, the serialization process seems to break partway through. This affects both self-closing elements and elements with children.

### Expected behavior

The MDX JSX elements should be properly serialized to their markdown representation, with all attributes correctly formatted and the closing tags properly rendered.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
