# Bug Report

### Describe the bug

The indentation in generated MDX output is incorrect. When rendering nested elements, the indentation level appears to be off by one, and elements at depth 0 are being indented with a single space instead of having no indentation.

### Reproduction

```js
// Create a nested MDX structure
const mdxTree = {
  type: 'root',
  children: [
    {
      type: 'element',
      depth: 0,
      children: [
        {
          type: 'element', 
          depth: 1,
          children: []
        }
      ]
    }
  ]
}

// Render the tree
const output = renderMdx(mdxTree)

// Expected: Root element has no indentation, nested element has 1 indent level
// Actual: Root element has 1 space, nested element has no indentation
```

### Expected behavior

- Elements at depth 0 should have no indentation (empty string)
- Elements at depth 1 should have 1 level of indentation
- Elements at depth 2 should have 2 levels of indentation
- And so on...

Currently it seems like the indentation is being reduced by 1 for all depths, and depth 0 is getting a single space character instead of being empty.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
