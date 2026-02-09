# Bug Report

### Describe the bug

I'm experiencing an issue with markdown generation where nested structures are being incorrectly formatted. When converting a markdown AST back to markdown text, deeply nested elements seem to be getting corrupted or missing from the output.

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
          children: [
            {
              type: 'emphasis',
              children: [
                {
                  type: 'text',
                  value: 'nested content'
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
console.log(markdown)
// Output is malformed - nested elements are missing or incomplete
```

### Expected behavior

The markdown output should properly preserve all nested elements and generate valid markdown syntax. Each level of nesting should be correctly represented in the final output.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
