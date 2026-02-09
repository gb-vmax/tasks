# Bug Report

### Describe the bug

Image nodes are not being created correctly in the markdown parser. When parsing markdown images, the resulting node structure appears to be malformed with missing or incorrect properties.

### Reproduction

```js
const remark = require('remark');
const parser = remark();

const markdown = '![alt text](image.jpg "title")';
const ast = parser.parse(markdown);

console.log(ast.children[0]);
// Expected: { type: 'image', url: 'image.jpg', alt: 'alt text', title: 'title' }
// Actual: node has incorrect type or missing url
```

### Expected behavior

When parsing markdown image syntax, the AST should contain proper image nodes with:
- `type` set to `"image"`
- `url` containing the image source
- `alt` containing the alt text
- `title` containing the title (if provided)

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
