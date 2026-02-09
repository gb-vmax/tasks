# Bug Report

### Describe the bug
After a recent update, image nodes in markdown are being rendered with the wrong type. When parsing markdown with images, the AST node type is coming back as `"img"` instead of the expected `"image"` type, which breaks downstream processing that relies on the correct node type.

### Reproduction
```js
const remark = require('remark');
const processor = remark();

const markdown = '![alt text](image.png "title")';
const ast = processor.parse(markdown);

// Find the image node
const imageNode = ast.children[0].children[0];
console.log(imageNode.type); // Outputs: "img" (incorrect)
// Expected: "image"
```

### Expected behavior
Image nodes should have `type: "image"` to match the standard mdast specification and maintain backwards compatibility with existing code that processes markdown AST nodes.

### Additional context
This is causing issues with plugins and transformers that check for `node.type === 'image'`. The change also affects the `alt` property which is now an empty string instead of `null` by default.

---
Repository: /testbed
