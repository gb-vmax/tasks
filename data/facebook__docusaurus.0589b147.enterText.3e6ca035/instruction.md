# Bug Report

### Describe the bug
I'm encountering an issue with text directives in remark-directive where parsing fails with a TypeError. When processing markdown content that contains text directives (inline directives with `:` syntax), the parser throws an error about calling a method on an undefined context.

### Reproduction
```js
import remarkDirective from 'remark-directive'
import remarkParse from 'remark-parse'
import { unified } from 'unified'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = 'Some text with :textdirective[content] inline'

// This throws an error when processing text directives
processor.parse(markdown)
```

### Expected behavior
The parser should successfully process text directives without throwing errors. Text directives should be parsed and added to the AST just like leaf and container directives.

### Additional context
This seems to affect only text directives (inline directives). Leaf directives (`::`) and container directives (`:::`) appear to work fine. The issue started appearing recently and I'm not sure what changed.

---
Repository: /testbed
