# Bug Report

### Describe the bug

I'm encountering an issue with text directives in remark-directive. When trying to parse markdown content containing text directives (like `:directive[content]`), the parser is throwing an error or not processing them correctly.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = 'This is a :text[directive] in a sentence.'

try {
  const result = processor.processSync(markdown)
  console.log(result)
} catch (error) {
  console.error('Error processing text directive:', error)
}
```

### Expected behavior

The text directive should be parsed correctly and added to the AST without any errors. The processor should handle inline text directives like `:text[content]` properly.

### Additional context

This seems to affect only text directives - leaf directives and container directives appear to work fine. The issue occurs when the parser tries to enter/process the text directive node.

---
Repository: /testbed
