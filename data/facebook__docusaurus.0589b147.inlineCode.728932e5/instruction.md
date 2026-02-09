# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering where the `data` property from the original markdown node is not being properly transferred to the resulting HTML element. The data seems to be applied to the text node instead of the code element itself.

### Reproduction

```js
const mdast = {
  type: 'inlineCode',
  value: 'example code',
  data: {
    hName: 'custom-code',
    hProperties: {
      className: ['highlight']
    }
  }
}

// Process this node through remark-rehype
// Expected: data applied to the <code> element
// Actual: data applied to the text node inside <code>
```

When processing inline code with custom `data` properties (like `hName` or `hProperties`), the custom properties are not appearing on the `<code>` element where they should be. Instead, they seem to be getting lost or applied incorrectly.

### Expected behavior

The `data` properties from the markdown inline code node should be applied to the resulting `<code>` HTML element, not to its child text node. This is important for cases where you want to customize the code element's tag name or add custom properties/classes.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
