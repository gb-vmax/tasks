# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark where container labels are not being processed correctly. When using directives with labels, the parser seems to lose track of the token context during the exit phase.

### Reproduction

```js
const remark = require('remark')
const directive = require('remark-directive')

const markdown = `
:::note[Important]
This is a note with a label
:::
`

const result = remark()
  .use(directive)
  .processSync(markdown)

console.log(result)
```

When parsing directives that have container labels (like `:::note[Important]`), the output structure appears malformed or incomplete. The label information seems to get lost or incorrectly processed.

### Expected behavior

The parser should correctly handle the exit of container label tokens and maintain proper token context throughout the parsing process. The resulting AST should include the complete label information for the directive.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
