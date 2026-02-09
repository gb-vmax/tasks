# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where code blocks with exactly 4 spaces of indentation are not being recognized correctly. The parser seems to be treating them differently than expected.

### Reproduction

```mdx
    const example = 'test';
    console.log(example);
```

When I have a code block indented with exactly 4 spaces (standard markdown indented code block), it's not being parsed as a code block. However, if I add 5 or more spaces, it works as expected.

### Expected behavior

According to the CommonMark spec, 4 spaces should be sufficient to create an indented code block. The parser should recognize and properly handle code blocks with exactly 4 spaces of indentation.

### Additional context

This seems to have started happening recently. I'm using `@mdx-js/mdx` version 3.0.0. The issue appears to be related to how the tokenizer checks the line prefix length for code indentation.

---
Repository: /testbed
