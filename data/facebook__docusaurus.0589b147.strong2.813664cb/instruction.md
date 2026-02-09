# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where strong elements (bold text) are sharing the same children array across multiple instances. When I have multiple bold sections in my MDX content, they all end up displaying the same content - specifically, the content from the last bold section appears in all of them.

### Reproduction

```mdx
This is **first bold text** and **second bold text** in the same document.
```

Expected output: Two separate bold sections with different text.

Actual output: Both bold sections show "second bold text".

It seems like all strong elements are referencing the same children array instead of having their own independent arrays. This causes all bold text in a document to display identical content.

### Expected behavior

Each strong element should have its own independent children array so that different bold sections can contain different text content. The compiled output should correctly preserve the distinct text for each bold element.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
