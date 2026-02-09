# Bug Report

### Describe the bug

I'm experiencing an issue with image parsing in remark where inline images are being incorrectly treated as image references, and vice versa. The parser seems to be confusing the two types of image syntax.

### Reproduction

```js
const remark = require('remark');

// Regular inline image
const markdown1 = '![alt text](https://example.com/image.png)';
const result1 = remark.parse(markdown1);
console.log(result1); // Expected: image node, but getting imageReference

// Image reference
const markdown2 = '![alt text][ref]';
const result2 = remark.parse(markdown2);
console.log(result2); // Expected: imageReference node, but getting image
```

### Expected behavior

- `![alt](url)` syntax should produce an `image` node with `url` and `title` properties
- `![alt][ref]` syntax should produce an `imageReference` node with `identifier`, `label`, and `referenceType` properties

Instead, the node types and properties are swapped - inline images are being parsed as references and references are being parsed as inline images.

### System Info

- remark version: 15.0.1
- Node.js version: 18.x

This is causing issues in my markdown processor where images aren't rendering correctly. Any help would be appreciated!

---
Repository: /testbed
