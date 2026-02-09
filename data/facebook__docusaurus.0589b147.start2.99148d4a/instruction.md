# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX files. After a recent update, code blocks are no longer being parsed correctly and the content is not rendering as expected.

### Reproduction

```mdx
# Test Document

Some text here.

```js
const example = "test";
console.log(example);
```

More text after the code block.
```

When processing this MDX content, the fenced code block doesn't get tokenized properly and either throws an error or fails to render the code block entirely.

### Expected behavior

The fenced code block should be properly recognized and rendered. The tokenizer should process the opening sequence (the triple backticks) and return control flow correctly to continue parsing the code block content.

### Additional context

This seems to affect all fenced code blocks regardless of the language specified. The issue appears to be in the tokenization phase where the opening fence sequence is being processed.

---
Repository: /testbed
