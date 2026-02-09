# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. It seems that code blocks with exactly 3 backticks or tildes are not being recognized properly anymore.

### Reproduction

```markdown
```js
console.log('test');
```
```

When I try to parse markdown with a standard 3-backtick fenced code block like above, it's not being tokenized correctly. The parser appears to be rejecting valid fenced code blocks.

Also noticed that closing fences with the same number of characters as the opening fence don't work properly:

```markdown
````
code here
````
```

The closing fence with 4 backticks should close the block that was opened with 4 backticks, but it's not matching correctly.

### Expected behavior

- Fenced code blocks with exactly 3 backticks/tildes should be valid (this is the standard markdown syntax)
- A closing fence with the same number of characters as the opening fence should properly close the code block

### System Info
- remark version: 15.0.1

---
Repository: /testbed
