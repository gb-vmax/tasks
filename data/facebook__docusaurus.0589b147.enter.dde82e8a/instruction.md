# Bug Report

### Describe the bug
I'm experiencing an issue with markdown serialization where nested structures aren't being properly tracked. When converting AST nodes to markdown, the output seems to be missing proper nesting context, causing formatting issues with nested elements like lists, blockquotes, and other block-level elements.

### Reproduction
```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'blockquote',
      children: [
        {
          type: 'paragraph',
          children: [{ type: 'text', value: 'nested content' }]
        }
      ]
    }
  ]
}

const markdown = toMarkdown(tree)
// Output is incorrectly formatted - nesting context is lost
```

### Expected behavior
Nested markdown elements should maintain their proper indentation and structure. For example, paragraphs inside blockquotes should be properly indented, and nested lists should have correct spacing.

The serialization should correctly track the depth/context as it traverses the AST tree so that nested elements are formatted appropriately.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
