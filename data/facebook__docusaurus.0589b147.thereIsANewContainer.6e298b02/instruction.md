# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where nested container blocks (like block quotes, lists, etc.) are not being handled correctly. When there's a new container that should be opened, the flow seems to be closing at the wrong time and the continuation logic appears broken.

### Reproduction

```mdx
> This is a blockquote
> with multiple lines
>
> - nested list item
> - another item

Regular paragraph after
```

When parsing the above MDX content, the nested structures don't render properly. The blockquote seems to close prematurely and the nested list items aren't being associated with the correct parent container.

### Expected behavior

The parser should correctly handle nested container blocks. When a new container is detected, it should:
1. Only close the flow if there's an active child flow
2. Exit the appropriate number of containers based on continuation
3. Continue document parsing with the proper nesting structure intact

The nested list should remain inside the blockquote, and all content should maintain its proper hierarchy.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - the same MDX content was working fine before. Any help would be appreciated!

---
Repository: /testbed
