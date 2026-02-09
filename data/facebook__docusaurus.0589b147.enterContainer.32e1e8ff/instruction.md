# Bug Report

### Describe the bug
I'm experiencing an issue with container directives in remark-directive. When processing markdown with container directives (like `:::note` blocks), the parser appears to be failing or producing incorrect output. The directives are not being properly converted to the expected AST nodes.

### Reproduction
```js
import {remark} from 'remark'
import remarkDirective from 'remark-directive'

const markdown = `
:::note
This is a container directive
:::
`

const result = remark()
  .use(remarkDirective)
  .processSync(markdown)

console.log(result)
```

### Expected behavior
Container directives should be parsed correctly and converted to proper `containerDirective` nodes in the AST. The output should maintain the directive structure and allow for proper serialization back to markdown.

### Additional context
This seems to have started recently. Leaf directives (`:directive`) and text directives (`::directive`) appear to work fine, but container directives specifically are affected.

---
Repository: /testbed
