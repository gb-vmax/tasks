# Bug Report

### Describe the bug

When parsing fenced code blocks with metadata in markdown, the metadata content is not being captured properly. The parser seems to skip directly to the next line instead of processing the metadata string that follows the language identifier.

### Reproduction

```markdown
```javascript meta information here
const x = 1;
```
```

When processing the above markdown, the metadata "meta information here" is not being tokenized. The parser moves to `infoBefore` immediately without consuming the metadata content.

### Expected behavior

The metadata portion of a fenced code block should be properly tokenized and stored in the AST. The parser should:
1. Detect the metadata after the language identifier
2. Enter the "codeFencedFenceMeta" token
3. Process the metadata string content
4. Then proceed to the code block body

Currently, it appears the metadata is being skipped entirely.

### Additional context

This affects any markdown processing that relies on code block metadata, such as:
- Syntax highlighting options
- Code block titles
- Custom attributes for code blocks

---
Repository: /testbed
