# Bug Report

### Describe the bug
Inline code blocks with backticks are not rendering correctly in markdown. When using multiple backticks to denote inline code, the opening sequence appears to be malformed or incomplete.

### Reproduction
```markdown
This is some text with ``inline code`` using double backticks.
```

Or with triple backticks:
```markdown
Here is ```some code``` with triple backticks.
```

### Expected behavior
The inline code should be properly parsed and rendered with the correct opening and closing backtick sequences. The parser should correctly identify the complete backtick sequence before moving to the content between the delimiters.

### Additional context
This seems to affect inline code (backtick sequences) specifically. Regular code blocks with fenced syntax appear to work fine. The issue manifests when trying to use multiple backticks to wrap inline code that itself contains backticks.

---
Repository: /testbed
