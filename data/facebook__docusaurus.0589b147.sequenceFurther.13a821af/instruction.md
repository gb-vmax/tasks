# Bug Report

### Describe the bug
I'm experiencing an issue with parsing ATX-style headings (headings with `#` symbols) in markdown. When using multiple `#` characters in sequence, the parser seems to stop processing after the first character instead of consuming the entire sequence.

### Reproduction
```markdown
## This is a heading
### Another heading
#### Fourth level heading
```

When parsing these headings, the sequence of `#` characters is not being fully consumed before moving to the next parsing stage. This causes the heading level to be incorrectly determined - it appears to only recognize the first `#` and then immediately proceed, rather than counting all consecutive `#` symbols.

### Expected behavior
The parser should consume all consecutive `#` characters at the beginning of a heading line to correctly determine the heading level. For example:
- `##` should be recognized as a level 2 heading
- `###` should be recognized as a level 3 heading
- `####` should be recognized as a level 4 heading

Currently, it seems like the sequence processing is terminating prematurely.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
