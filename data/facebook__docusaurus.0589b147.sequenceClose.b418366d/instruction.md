# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in MDX. When using multiple backticks for inline code (like ``` `` ``` for code containing a single backtick), the parser doesn't correctly match the closing sequence.

### Reproduction

```mdx
This is some text with ``code containing a ` backtick`` more text.
```

The inline code block doesn't get properly closed, and the rest of the content is incorrectly treated as part of the code block.

Another example:
```mdx
Use ```two backticks``` in your code
```

The parser seems to have trouble when the number of opening and closing backticks should match but doesn't behave as expected.

### Expected behavior

The parser should correctly match opening and closing backtick sequences of the same length. A code span opened with N backticks should only close when it encounters N consecutive backticks again (not counting any backticks that are part of the code content itself).

For example, ``` ``code`` ``` should parse as inline code containing the text "code", and ``` ``code with ` backtick`` ``` should parse as inline code containing "code with ` backtick".

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
