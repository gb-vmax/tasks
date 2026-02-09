# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence sequence is not being recognized correctly. When I have a code block with the same number of backticks/tildes in the opening and closing fence, the closing fence is not properly detected and the code block doesn't close.

### Reproduction

```markdown
~~~
some code content
~~~
```

The above code block with exactly 3 tildes for both opening and closing should be valid, but it's not being parsed correctly. The closing fence with the same number of characters as the opening fence should close the block, but it seems to require more characters than the opening sequence.

### Expected behavior

A fenced code block should close when the closing fence has the same number of fence characters (backticks or tildes) as the opening fence. This is standard Markdown/CommonMark behavior.

For example:
- ` ``` ` should close with ` ``` `
- ` ~~~~ ` should close with ` ~~~~ `

Currently it appears the closing fence needs to have MORE characters than the opening, which breaks standard markdown documents.

### Additional context

This affects any fenced code blocks where the opening and closing sequences have the exact same length. It's causing valid markdown files to not render properly.

---
Repository: /testbed
