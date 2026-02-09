# Bug Report

### Describe the bug

I'm encountering an issue with paragraph parsing where the content structure seems to be broken. When processing markdown paragraphs, the parser appears to be entering states incorrectly, which causes problems with how paragraph content is being tokenized.

### Reproduction

```js
const markdown = `This is a simple paragraph.

Another paragraph here.`;

// Parse the markdown
const result = remark().parse(markdown);

// The paragraph tokens don't have the expected structure
// Content is not properly wrapped in paragraphContent tokens
```

### Expected behavior

Paragraphs should be properly tokenized with the correct nested structure. The parser should enter the paragraph state and then properly handle the content within it.

### Additional context

This seems to affect how paragraph content is being tracked during the parsing phase. The tokenization flow appears to skip important state transitions when initializing paragraph content.

---
Repository: /testbed
