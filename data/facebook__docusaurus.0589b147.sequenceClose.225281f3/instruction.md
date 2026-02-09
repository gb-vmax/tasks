# Bug Report

### Describe the bug

Code fences in Markdown are not closing properly when the closing fence has more backticks/tildes than the opening fence. According to the CommonMark spec, a code fence should only be closed by a fence sequence that has at least as many characters as the opening fence, not more.

### Reproduction

```markdown
````js
const code = 'test';
`````
```

The above code fence with 4 backticks in the opening should NOT be closed by the 5 backtick closing fence. However, it's currently being treated as closed.

Another example:
```markdown
~~~markdown
# Header
~~~~
```

The 3-tilde opening fence is being incorrectly closed by a 4-tilde sequence.

### Expected behavior

According to the CommonMark specification, a closing code fence must use the same character as the opening fence and must be at least as long as the opening fence, but **not longer**. The closing fence should have exactly the same or fewer characters than the opening fence to properly close it.

In the examples above:
- A 4-backtick opening should only be closed by exactly 4 backticks (or more backticks should be treated as part of the code content)
- A 3-tilde opening should only be closed by exactly 3 tildes (4 tildes should not close it)

### System Info
- @mdx-js/mdx version: 3.0.0
- Using Jest vendor bundle

---
Repository: /testbed
