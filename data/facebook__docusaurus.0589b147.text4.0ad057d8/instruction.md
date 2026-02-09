# Bug Report

### Describe the bug

I'm experiencing an issue with text node creation in the markdown parser. When parsing markdown content, I'm getting errors about text nodes not being properly formatted. It seems like the parser is returning a function instead of an actual text node object in some cases.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
This is a simple text paragraph.

Another paragraph here.
`;

const ast = processor.parse(markdown);
console.log(ast);
```

When running this, the AST contains unexpected function objects where text nodes should be. This causes downstream processing to fail when trying to access properties like `type` or `value` on what should be text nodes.

### Expected behavior

The parser should consistently return text node objects with the structure:
```js
{
  type: "text",
  value: "some text content"
}
```

Instead, it sometimes returns a function that needs to be called to get the actual node object.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is breaking our markdown rendering pipeline. Any help would be appreciated!

---
Repository: /testbed
