# Bug Report

### Describe the bug

I'm encountering an issue with image syntax parsing in MDX. When trying to use the standard markdown image syntax `![alt text](url)`, it's not being recognized correctly. The parser seems to be looking for the wrong character code when tokenizing image labels.

### Reproduction

```markdown
![Example Image](https://example.com/image.png)
```

When processing this MDX content, the image syntax is not parsed as expected. The opening bracket sequence `![` should be recognized as the start of an image label, but it appears the tokenizer is checking for the wrong character.

### Expected behavior

The standard markdown image syntax `![alt](url)` should be properly tokenized and converted to the appropriate image element. The opening `![` should be recognized as the label marker for an image.

### Additional context

This seems related to the label tokenization logic. The character code for `[` is 91, but something in the parsing flow might be checking for a different character instead.

---
Repository: /testbed
