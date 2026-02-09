# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When using backticks to create inline code snippets, the parser seems to be handling the backtick sequences incorrectly, causing the code text to not be properly recognized.

### Reproduction

```markdown
This is `inline code` in a sentence.
```

When parsing the above markdown, the inline code block is not being processed correctly. It appears that the tokenizer is not properly consuming the opening backtick sequence.

### Expected behavior

The parser should correctly identify and tokenize inline code blocks surrounded by backticks. The opening backtick sequence should be fully consumed before moving to process the content between the backticks.

For example:
- Input: `` `code` ``
- Expected: Properly parsed inline code node with content "code"
- Actual: Incorrect parsing behavior

### Additional context

This seems to be related to how the code text tokenizer handles the sequence of backtick characters. The issue manifests when trying to parse any inline code, regardless of the number of backticks used.

---
Repository: /testbed
