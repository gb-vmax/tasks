# Bug Report

### Describe the bug

I'm experiencing issues with directive parsing in remark-directive. It seems like directive names and labels are getting swapped, and text directives aren't being processed correctly.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

// Container directive with label
const markdown = ':::note[This is a label]{#id}\nContent here\n:::'
const ast = processor.parse(markdown)
const result = processor.runSync(ast)

console.log(result)
// The name and label properties appear to be swapped in the output
```

When parsing container directives, the `name` property seems to contain what should be the `label`, and vice versa. Also noticed that inline text directives (like `:text[content]`) are not being recognized properly - they don't seem to be marked as elements that can contain EOLs.

### Expected behavior

- Container directive names should be stored in the `name` property
- Container directive labels should be stored in the `label` property  
- Text directives should be able to contain end-of-line characters

### System Info

- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
