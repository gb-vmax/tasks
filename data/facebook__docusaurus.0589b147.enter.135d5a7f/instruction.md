# Bug Report

### Describe the bug

I'm experiencing an issue with nested markdown structures where the state stack isn't being managed correctly. When processing deeply nested elements (like lists within lists or nested blockquotes), the exit function appears to be removing the wrong items from the stack.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'list',
      children: [
        {
          type: 'listItem',
          children: [
            {
              type: 'list',
              children: [
                {
                  type: 'listItem',
                  children: []
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

const result = toMarkdown(tree)
// Output is malformed or throws an error
```

### Expected behavior

When entering and exiting nested structures with the same name (e.g., multiple 'list' or 'listItem' nodes), the stack should properly track each level and remove only the most recently added item when exiting, maintaining the correct nesting hierarchy.

### Additional context

This seems to happen specifically when you have multiple nested nodes of the same type. The stack management doesn't follow LIFO (last-in-first-out) order properly, which causes issues when rendering complex nested markdown structures.

---
Repository: /testbed
