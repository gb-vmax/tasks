# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX. When using backticks for inline code, the parser seems to be closing the code span too early when there are multiple consecutive backticks.

### Reproduction

```mdx
This is some text with `inline code` that works fine.

But this ``code with double backticks`` doesn't parse correctly.

And this ```triple backtick code``` also has issues.
```

The problem appears when the number of closing backticks is greater than or equal to the opening backticks. The code span gets closed prematurely, leaving extra backticks as plain text in the output.

### Expected behavior

Inline code should only close when the exact same number of backticks is encountered. For example:
- `` `code` `` should require exactly one backtick to close
- `` ``code`` `` should require exactly two backticks to close  
- `` ```code``` `` should require exactly three backticks to close

Currently it seems like any sequence of backticks equal to or longer than the opening sequence will close the code span, which breaks the rendering.

### System Info
- MDX version: 3.0.0
- Using the micromark tokenizer for code text

---
Repository: /testbed
