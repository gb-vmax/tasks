# Bug Report

### Describe the bug
I'm encountering an issue with ATX heading parsing where the parser seems to be consuming heading content incorrectly. After parsing heading text, the parser appears to be stuck in an incorrect state instead of continuing to process the rest of the heading properly.

### Reproduction
```markdown
# This is a heading with some text
```

When parsing ATX headings (markdown headings with `#` symbols), the content after the heading sequence doesn't get processed correctly. The parser consumes characters from the heading text but then seems to break out of the data processing loop prematurely.

### Expected behavior
The parser should correctly consume all the heading text characters and continue processing until it encounters a valid termination condition (like end of line or closing `#` symbols). The heading content should be fully captured and the parser should transition to the appropriate next state.

### Additional context
This appears to affect how headings are tokenized. The issue manifests when there's text content in the heading - the parser's state transitions seem off, causing it to not properly handle the character stream after consuming heading text.

---
Repository: /testbed
