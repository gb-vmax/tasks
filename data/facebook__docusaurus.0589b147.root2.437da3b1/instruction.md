# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where the order of child elements appears to be incorrect when certain conditions are met. It seems like elements that should appear after queued content are instead appearing before it.

### Reproduction

When processing MDX content with a mix of different element types, the output order doesn't match the expected structure. Specifically, when there are elements that get queued followed by regular elements, the regular elements end up in the wrong position relative to the queued content.

For example, if you have a structure like:
```mdx
<Component1 />
<Component2 />
<Component3 />
```

Where Component2 triggers queueing behavior, Component3 might appear before Component2's queued children instead of after them.

### Expected behavior

Child elements should maintain their proper order in the output, with queued elements being inserted at the correct position relative to non-queued siblings.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
