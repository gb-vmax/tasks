# Bug Report

### Describe the bug

I'm encountering an issue with HTML closing tags in markdown parsing. When processing HTML closing tags (e.g., `</div>`), the parser seems to behave incorrectly - it's either consuming characters it shouldn't or following an unexpected code path.

### Reproduction

```js
const markdown = `
<div>
  Some content
</div>
`

// Parse the markdown with HTML tags
const result = remark().parse(markdown)
```

The closing tag `</div>` is not being parsed correctly. It appears the tokenizer is handling the alphabetic character after `</` in an unexpected way.

### Expected behavior

HTML closing tags should be properly tokenized and parsed. The closing tag should be recognized as a valid HTML element and the content should be processed accordingly.

### Additional context

This seems to affect any HTML closing tag in markdown content. The issue appears to be in the `tagCloseStart` function of the HTML text tokenizer, where the logic for handling alphabetic characters after the `</` sequence may not be correct.

---
Repository: /testbed
