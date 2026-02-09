# Bug Report

### Describe the bug

I'm encountering an issue with markdown code fence parsing. When I have code blocks in my markdown files, they're not being recognized correctly. Specifically, code fences that should be open are being treated as closed, and the fence character detection seems to be picking the wrong character.

### Reproduction

```markdown
~~~javascript
const example = 'test';
~~~
```

When parsing this markdown, the code fence isn't being properly detected. The parser seems to be looking at the wrong position in the fence string to determine the fence type (backticks vs tildes).

Also, code fences that are definitely open (have content on the same line as the opening fence) are being marked as not open, and vice versa.

### Expected behavior

- The parser should correctly identify whether a fence uses backticks (`) or tildes (~)
- Code fences with content on the opening line should be marked as `definitelyOpen: true`
- Code fences without content on the opening line should be marked as `definitelyOpen: false`

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently and is affecting all my markdown documentation pages with code blocks.

---
Repository: /testbed
