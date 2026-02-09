# Bug Report

### Describe the bug

I'm experiencing an issue with link rendering where the `data` property from markdown AST nodes is not being applied correctly to the resulting HTML links. When I have markdown links with custom data attributes, they're not appearing in the final output.

### Reproduction

```js
const markdown = '[Link text](https://example.com)'
// Assuming the AST node has data properties attached

const ast = {
  type: 'link',
  url: 'https://example.com',
  data: {
    hProperties: {
      className: ['custom-link']
    }
  },
  children: [{ type: 'text', value: 'Link text' }]
}

// After transformation, the data properties are missing from the output
// Expected: <a href="https://example.com" class="custom-link">Link text</a>
// Actual: <a href="https://example.com">Link text</a>
```

### Expected behavior

Custom data properties attached to link nodes in the markdown AST should be properly transferred to the HTML output. The `data.hProperties` should be merged into the resulting anchor element's properties.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
