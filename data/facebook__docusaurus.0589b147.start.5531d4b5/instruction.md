# Bug Report

### Describe the bug
Image markdown syntax is not being parsed correctly. When trying to use image links like `![alt text](url)`, the parser seems to fail or produce unexpected results.

### Reproduction
```js
const markdown = '![test image](https://example.com/image.png)';
// Parser fails to correctly handle the image syntax
```

I noticed this after a recent update. The image markdown syntax `![...]` appears to be broken - it's either not recognized at all or causes the parser to stop processing.

### Expected behavior
The parser should correctly recognize and process image markdown syntax `![alt](url)` and convert it to the appropriate output format.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
