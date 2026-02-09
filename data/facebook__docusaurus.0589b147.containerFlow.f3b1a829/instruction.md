# Bug Report

### Describe the bug

I'm experiencing an issue with markdown list formatting when using the remark processor. When I have nested lists or multiple list items, the output is not being formatted correctly. It seems like list markers are being reset or cleared unexpectedly between list items.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
- Item 1
- Item 2
  - Nested item 1
  - Nested item 2
- Item 3
`

const result = await remark().process(markdown)
console.log(String(result))
```

When processing lists with multiple items, especially nested lists, the bullet markers don't maintain consistency. The processor seems to be losing track of which bullet style was last used between list items.

### Expected behavior

The list should maintain consistent bullet markers throughout, and nested lists should preserve their formatting structure. The `bulletLastUsed` state should only be cleared when moving out of list context, not between list items within the same list.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is affecting our documentation generation pipeline. Any help would be appreciated!

---
Repository: /testbed
