# Bug Report

### Describe the bug

After a recent update, markdown parsing seems to be completely broken. The tokenizer is not processing constructs properly and parsing fails silently without generating the expected AST nodes.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `# Hello World

This is a test paragraph.`

const result = remark().parse(markdown)
console.log(result)
// Expected: Full AST with heading and paragraph nodes
// Actual: Empty or incomplete AST
```

### Expected behavior

The parser should successfully tokenize and create AST nodes for all markdown constructs (headings, paragraphs, lists, etc.). The parsed result should contain a complete syntax tree representation of the input markdown.

### Additional context

This appears to affect all markdown constructs. Even simple headings and paragraphs are not being parsed correctly. The issue started appearing after the latest changes to the tokenizer logic.

---
Repository: /testbed
