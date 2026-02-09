# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links are being incorrectly converted to reference-style links (or vice versa). The link nodes in the AST seem to have the wrong type and properties after parsing.

### Reproduction

```js
const remark = require('remark');

const markdown = `[example link](https://example.com)`;
const ast = remark.parse(markdown);

// The link node has incorrect type or missing properties
console.log(ast.children[0].children[0]);
```

When parsing regular inline links with URLs, they're being treated as reference links, or reference links are being treated as regular links. The node structure ends up with the wrong combination of properties (url/title vs identifier/label).

### Expected behavior

- Regular links `[text](url)` should have `type: 'link'` with `url` and `title` properties
- Reference links `[text][ref]` should have `type: 'linkReference'` with `identifier` and `label` properties

The parser should correctly distinguish between these two link types and generate the appropriate AST nodes.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
