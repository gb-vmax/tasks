# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When I include a fenced code block in my markdown content, the parser seems to be processing the content incorrectly and not properly detecting the end of the code block.

### Reproduction

```markdown
```js
console.log('test');
```
```

When parsing the above markdown, the code block content is not being handled correctly. It appears that the parser is continuing to process content that should be part of the code block as if it were regular markdown.

### Expected behavior

The parser should correctly identify and parse fenced code blocks, treating everything between the opening and closing fence markers as code content. The content inside the code block should be preserved as-is without being interpreted as markdown.

### Additional context

This seems to affect code blocks with any language identifier (js, python, etc.). The issue appears to be related to how the parser determines whether it's inside or outside of a code block.

---
Repository: /testbed
