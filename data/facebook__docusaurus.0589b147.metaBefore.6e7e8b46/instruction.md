# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a code fence has an info string but no metadata, the parser seems to be entering the wrong state or not handling the case properly.

### Reproduction

```markdown
```javascript
const x = 1;
```
```

The issue occurs when parsing fenced code blocks that have a language identifier (info string) but no additional metadata after it. The parser appears to be incorrectly handling the case when it encounters a line ending immediately after the info string.

### Expected behavior

The parser should correctly handle fenced code blocks with just an info string (language identifier) and no metadata. The code block should be parsed successfully and the content should be accessible.

### Additional context

This seems to affect basic markdown code blocks which is a pretty common use case. Not sure if this is related to recent changes in the tokenizer logic but it's causing parsing issues for standard markdown syntax.

---
Repository: /testbed
