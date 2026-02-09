# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where the label markers aren't being processed correctly. It seems like the parser gets stuck in an infinite loop when trying to parse directive labels.

### Reproduction

When parsing markdown with directives that contain labels, the parser enters an infinite loop and never completes:

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

// This hangs indefinitely
const result = processor.processSync('::directive[label text]')
```

### Expected behavior

The directive with its label should be parsed successfully without hanging. The parser should properly tokenize the opening bracket, label content, and closing bracket.

### Additional context

This appears to affect any directive syntax that includes square bracket labels. The parser seems to get stuck at the start of label processing and never progresses to actually reading the label content.

---
Repository: /testbed
