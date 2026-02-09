# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings are not being recognized correctly. It seems like the heading structure is not being properly initialized, causing the parser to fail when encountering ATX-style headings (lines starting with `#`).

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown content, the headings are not being processed correctly. The parser appears to skip over them or doesn't recognize them as valid heading elements.

### Expected behavior

ATX headings should be properly parsed and converted to their corresponding heading elements. The parser should enter the heading state and process the sequence of `#` characters followed by the heading text.

### Additional context

This issue affects all ATX heading levels (h1 through h6). The problem seems to be related to how the heading tokenization is initialized - the heading entry point might not be getting set up properly before processing begins.

---
Repository: /testbed
