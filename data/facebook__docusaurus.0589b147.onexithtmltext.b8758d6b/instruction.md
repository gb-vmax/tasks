# Bug Report

### Describe the bug

I'm experiencing an issue with HTML text parsing in markdown. When I include HTML in my markdown content, the parsed output is incorrect - the HTML text content seems to be assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = `
Some text before

<div>Hello World</div>

Some text after
`;

// Parse the markdown
const result = parse(markdown);

// The HTML text "Hello World" is not where it should be in the AST
// It appears to be attached to the wrong parent node
```

### Expected behavior

The HTML text content should be properly attached to the correct node in the abstract syntax tree. Currently it seems like the data is being placed on a parent or sibling node instead of the actual HTML text node.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is causing issues when trying to process or transform markdown documents that contain inline HTML elements. The resulting AST structure doesn't match what's expected.

---
Repository: /testbed
