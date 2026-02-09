# Bug Report

### Describe the bug

I'm encountering an issue with image parsing in markdown. When parsing markdown images, the resulting AST nodes have an incorrect `type` field. Instead of getting `"image"` as the type, I'm seeing `"img"` which breaks downstream processing that expects standard markdown AST format.

### Reproduction

```js
const processor = remark();
const ast = processor.parse('![alt text](image.jpg "title")');

// The image node has type: "img" instead of type: "image"
console.log(ast.children[0].type); // Expected: "image", Got: "img"
```

Also noticing that the `url` field is being set to `null` instead of an empty string `""` for images without a URL, which is inconsistent with how other node types handle empty values.

### Expected behavior

Image nodes should have `type: "image"` to match the standard markdown AST specification, and the `url` field should default to an empty string rather than `null`.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
