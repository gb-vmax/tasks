# Bug Report

### Describe the bug

I'm experiencing an issue with markdown serialization where the output appears to be incomplete or malformed when converting certain AST structures back to markdown. It seems like the internal state management isn't properly cleaning up after processing nested structures, causing some elements to persist in the stack when they shouldn't.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        {
          type: 'strong',
          children: [
            { type: 'text', value: 'bold text' }
          ]
        }
      ]
    }
  ]
};

const result = toMarkdown(tree);
// Result is not properly formatted
```

### Expected behavior

The markdown output should correctly serialize nested structures and properly close all formatting tags. The internal stack should be empty after processing completes.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
