# Bug Report

### Describe the bug

HTML comments and declarations are not being parsed correctly in markdown text. After a recent update, it seems like the parser is confusing `<!` declarations (like `<!-- comments -->` or `<!DOCTYPE>`) with `<?` processing instructions.

### Reproduction

```markdown
This is a test with an HTML comment:
<!-- This should be a comment -->

And a DOCTYPE declaration:
<!DOCTYPE html>
```

When parsing the above markdown, the HTML comment and DOCTYPE declaration are not being recognized properly. The parser seems to be treating them as the wrong token type.

### Expected behavior

- `<!-- ... -->` should be parsed as HTML comments
- `<!DOCTYPE ...>` and other `<!` declarations should be parsed as declarations
- `<? ... ?>` should be parsed as processing instructions
- Regular HTML tags like `<div>` should still work normally

The parser should correctly distinguish between these different HTML constructs based on what follows the opening `<` character.

### System Info
- remark version: 15.0.1
- Browser: N/A (server-side parsing)

---
Repository: /testbed
