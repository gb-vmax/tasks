# Bug Report

### Describe the bug

Image links in markdown are not being parsed correctly. When trying to use the `![alt](url)` syntax, the parser seems to be closing the image node too early, which causes the rest of the image syntax to be interpreted incorrectly or not at all.

### Reproduction

```js
const markdown = '![test image](https://example.com/image.png)'

// Parse the markdown
const result = remark().parse(markdown)

// The image node structure is malformed
// Expected: proper labelImage node with nested labelMarker
// Actual: labelImage closes prematurely before labelMarker is processed
```

### Expected behavior

The markdown parser should correctly parse image syntax with the following structure:
1. Open `labelImage` 
2. Process `labelImageMarker` (the `!` character)
3. Process `labelMarker` (the `[` character)
4. Parse alt text
5. Parse URL
6. Close `labelImage` after all components are processed

Instead, the `labelImage` node is being closed immediately after the `labelImageMarker`, which breaks the expected AST structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
