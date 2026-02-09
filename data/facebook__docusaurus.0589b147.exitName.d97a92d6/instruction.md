# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in remark-directive where the directive name is not being set correctly. When parsing markdown with leaf directives (like `::leafDirective`), the name property appears to be empty or incorrectly assigned.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
::myLeafDirective
Content here
`

const ast = processor.parse(markdown)
const result = processor.runSync(ast)

console.log(result.children[0].name) // Expected: 'myLeafDirective', Actual: empty or undefined
```

### Expected behavior

The `name` property of leaf directive nodes should be properly populated with the directive name from the markdown source. Container and text directives seem to work fine, but leaf directives specifically are affected.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
