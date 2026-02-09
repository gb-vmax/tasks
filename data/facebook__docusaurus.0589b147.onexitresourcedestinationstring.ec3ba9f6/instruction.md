# Bug Report

### Describe the bug
I'm experiencing an issue with MDX link parsing where the URL destination is being assigned to the wrong node in the AST. When processing resource destination strings (like URLs in markdown links), the code appears to be accessing the first element of the stack instead of the last one, which causes the URL to be set on an incorrect parent node rather than the actual link node.

### Reproduction
```mdx
[Click here](https://example.com)
```

When the above MDX is processed, the link URL gets assigned to the wrong AST node. This happens because during the exit handler for resource destination strings, the code is looking at `this.stack[0]` (the root/first node) instead of `this.stack[this.stack.length - 1]` (the current link node being processed).

### Expected behavior
The URL should be correctly assigned to the link node that's currently being processed (the last item in the stack), not the first item in the stack. Links should render with their proper href attributes pointing to the correct destinations.

### Additional context
This appears to affect the `onexitresourcedestinationstring` function in the MDX compiler. The stack is used to track nested nodes during parsing, and accessing the wrong index means the URL property gets set on the wrong object entirely.

---
Repository: /testbed
