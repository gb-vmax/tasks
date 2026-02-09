# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I have multiple consecutive fenced code blocks in my markdown, the content is not being captured correctly. The first code block works fine, but subsequent code blocks appear to be empty or missing their content.

### Reproduction

```markdown
First code block:
```js
console.log('first');
```

Second code block:
```js
console.log('second');
```
```

When parsing this markdown, the second code block doesn't contain the expected code content.

### Expected behavior

Each fenced code block should independently capture and preserve its content, regardless of how many code blocks appear in the document. Both code blocks should contain their respective code strings.

### Additional context

This seems to have started happening recently. I'm using remark for markdown processing and the issue appears to be related to how the parser tracks whether it's inside a code fence or not.

---
Repository: /testbed
