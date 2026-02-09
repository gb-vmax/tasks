# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where line endings in setext headings are being handled incorrectly. The parser seems to be accessing the wrong stack level when processing line ending tokens, which causes unexpected behavior in the rendered output.

### Reproduction

```js
const markdown = `Heading
=======

Some content here`;

const result = remark().process(markdown);
// The output is malformed - line endings are not properly associated with their parent nodes
```

When parsing setext-style headings (underlined with `=` or `-`), the line ending processing appears to be looking at the wrong context in the parse stack. This results in incorrect positioning information and potentially malformed AST nodes.

### Expected behavior

Line endings should be properly handled during setext heading parsing, with the correct context node being referenced from the stack. The parser should correctly determine whether to slurp line endings based on the appropriate heading state.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
