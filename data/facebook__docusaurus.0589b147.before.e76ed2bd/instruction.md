# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading parsing where ATX headings (headings with `#` symbols) are not being processed correctly. The parser seems to be entering a state twice which is causing unexpected behavior.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown, the headings are not being recognized properly. It appears that something is being called twice during the tokenization phase, which breaks the normal flow.

### Expected behavior

ATX headings should be parsed correctly and converted to the appropriate heading elements. The tokenizer should enter each state exactly once as needed.

### Additional context

This seems to have started happening recently. The parsing logic for heading sequences appears to have been modified in a way that causes duplicate state entries. I noticed this when my markdown files with standard headings stopped rendering correctly.

---
Repository: /testbed
