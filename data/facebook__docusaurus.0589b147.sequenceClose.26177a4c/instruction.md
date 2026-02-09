# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX where fenced code blocks aren't being closed correctly when the closing fence has more backticks than the opening fence.

### Reproduction

```markdown
```js
const x = 1;
````
```

When parsing the above MDX content, the code block doesn't close properly. The closing fence with 4 backticks should close the opening fence with 3 backticks, but it seems like the parser is not recognizing it as a valid closing fence.

### Expected behavior

According to CommonMark spec, a closing code fence should have at least as many backticks as the opening fence. So a fence opened with 3 backticks (```) should be closeable by either 3 or more backticks (```, ````, etc.).

The parser should correctly identify when a closing fence has an equal or greater number of fence characters compared to the opening fence and properly close the code block.

### Additional context

This appears to be related to how the fence sequence counting logic works. The issue manifests when trying to use longer closing fences, which is a valid pattern in markdown/MDX for cases where you need to nest code blocks or include fence characters in your code examples.

---
Repository: /testbed
