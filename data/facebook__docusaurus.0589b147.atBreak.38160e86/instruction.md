# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in markdown. It seems like the parser is now treating all headings as if they continue indefinitely, even when they should be properly terminated.

### Reproduction

When parsing markdown with ATX-style headings (using `#` symbols), the heading content appears to consume the rest of the document instead of stopping at the line ending.

```markdown
# Heading One
Some paragraph text

## Heading Two
More content
```

The parser seems to be treating everything after the first heading as part of that heading's text, rather than recognizing the line ending and moving on to parse the subsequent content.

### Expected behavior

The parser should:
1. Recognize the heading sequence (`#` or `##`)
2. Parse the heading text until the end of the line
3. Exit the heading state when encountering a line ending (or null)
4. Continue parsing the rest of the document normally

Instead, it appears to be continuing to parse content as part of the heading when it shouldn't.

### Additional context

This affects all ATX-style headings in markdown documents. The heading parser doesn't seem to be properly detecting when to exit the heading state, causing it to incorrectly consume subsequent content.

---
Repository: /testbed
