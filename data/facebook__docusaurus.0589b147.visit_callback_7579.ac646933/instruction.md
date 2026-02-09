# Bug Report

### Describe the bug

I'm encountering an issue with heading formatting in markdown output. When converting markdown AST to string format, headings that should be formatted as setext-style (underlined with `=` or `-`) are incorrectly being formatted as ATX-style (with `#` symbols) in certain cases.

### Reproduction

```js
const mdast = {
  type: 'heading',
  depth: 2,
  children: [
    {
      type: 'text',
      value: 'Hello\nWorld'
    }
  ]
}

// Convert to markdown
const result = toMarkdown(mdast, { setext: true })

// Expected: Setext style heading with underline
// Actual: ATX style heading with ##
```

The issue occurs specifically when:
1. A heading contains text with line breaks
2. The setext option is enabled
3. The heading depth is 1 or 2

### Expected behavior

Headings with line breaks in their content should be formatted as setext-style (underlined) when the setext option is enabled and the heading depth is appropriate (1 or 2). The presence of literal line breaks in the heading text should trigger setext formatting.

### Additional context

This seems to affect how headings with multi-line content are detected and formatted. The formatting logic should recognize when a heading contains line breaks and apply setext style accordingly.

---
Repository: /testbed
