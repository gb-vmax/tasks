# Bug Report

### Describe the bug

I'm experiencing an issue with markdown serialization where deeply nested structures cause the serializer to fail. When processing markdown with multiple levels of nesting (like lists inside blockquotes inside other lists), the output becomes corrupted or the serializer throws an error.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'blockquote',
      children: [
        {
          type: 'list',
          children: [
            {
              type: 'listItem',
              children: [
                {
                  type: 'paragraph',
                  children: [{ type: 'text', value: 'nested item' }]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

const markdown = toMarkdown(tree)
// Expected: proper markdown output
// Actual: corrupted output or error
```

### Expected behavior

The serializer should handle deeply nested structures gracefully and produce valid markdown output regardless of nesting depth. The internal stack should maintain its structure throughout the serialization process.

### Additional context

This seems to happen specifically when exiting from deeply nested nodes. The serializer appears to lose track of the nesting context, resulting in malformed output.

---
Repository: /testbed
