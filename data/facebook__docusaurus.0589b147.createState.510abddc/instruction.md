# Bug Report

### Describe the bug

I'm experiencing an issue where markdown content with custom handlers is not being transformed correctly. The transformation seems to skip all registered handlers and only passes through certain node types. This results in incomplete or incorrect HTML output.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype, {
    handlers: {
      emphasis: (state, node) => {
        // Custom emphasis handler
        return { type: 'element', tagName: 'em', children: state.all(node) }
      },
      strong: (state, node) => {
        // Custom strong handler
        return { type: 'element', tagName: 'strong', children: state.all(node) }
      }
    }
  })

const result = processor.processSync('**bold** and *italic* text')
```

### Expected behavior

The custom handlers should be invoked for emphasis and strong nodes, transforming them into the appropriate HTML elements. Instead, it appears that nodes with registered handlers are being ignored completely.

### Additional context

This seems to affect all node types that have custom handlers registered. The transformation pipeline appears to be skipping over nodes instead of processing them with the provided handlers.

---
Repository: /testbed
