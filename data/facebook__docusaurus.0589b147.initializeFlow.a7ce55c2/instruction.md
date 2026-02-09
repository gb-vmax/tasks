# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content after blank lines is not being processed correctly. It seems like the parser is getting stuck or skipping content that should be parsed as flow content.

### Reproduction

```js
const markdown = `# Heading

Some paragraph text after a blank line.

Another paragraph.`

// Parse the markdown
const result = parse(markdown)

// The paragraphs after blank lines are missing or not parsed correctly
```

When there's a blank line followed by content, the content after the blank line doesn't get parsed properly. The parser seems to consume the line ending but then doesn't continue processing the subsequent content.

### Expected behavior

All content should be parsed correctly regardless of blank lines. The parser should continue processing flow content after encountering blank lines.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
