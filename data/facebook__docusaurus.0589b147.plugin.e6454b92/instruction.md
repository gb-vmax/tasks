# Bug Report

### Describe the bug

Mermaid code blocks are no longer being rendered correctly. After a recent update, all code blocks that are NOT mermaid are being transformed into mermaid diagrams, while actual mermaid code blocks are being ignored.

### Reproduction

Create an MDX file with both mermaid and non-mermaid code blocks:

````markdown
```mermaid
graph TD
  A --> B
```

```javascript
console.log('hello');
```
````

### Expected behavior

- The mermaid code block should be transformed into a mermaid diagram
- The javascript code block should remain as a regular code block

### Actual behavior

- The mermaid code block is NOT transformed and appears as plain text
- The javascript code block is incorrectly transformed as if it were a mermaid diagram

It seems like the logic for detecting mermaid code blocks got inverted somehow. Regular code blocks are being treated as mermaid and vice versa.

---
Repository: /testbed
