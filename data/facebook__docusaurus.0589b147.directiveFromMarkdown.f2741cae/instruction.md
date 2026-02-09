# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where leaf directives are not properly handling their attributes. After some recent changes, it seems like the attribute parsing for leaf-style directives (like `:directive[content]{attributes}`) is completely broken.

### Reproduction

```js
import {fromMarkdown} from 'mdast-util-from-markdown'
import {directiveFromMarkdown} from 'remark-directive'

const markdown = ':myDirective[some content]{#myId .myClass key=value}'

const tree = fromMarkdown(markdown, {
  extensions: [directiveExtension],
  mdastExtensions: [directiveFromMarkdown()]
})

console.log(tree)
// Expected: directive node with attributes object containing id, class, and key
// Actual: attributes are missing or undefined
```

When I try to parse markdown with leaf directives that have attributes, the resulting AST doesn't include the attribute information at all. The directive is recognized but the `attributes` property is either missing or empty.

### Expected behavior

Leaf directives should parse their attributes correctly, just like container and text directives do. The attributes (id, class, and custom key-value pairs) should be available in the resulting node.

### Additional context

This seems to have started happening recently. Container directives (:::) and text directives (:text:) still work fine with their attributes, but leaf directives (:directive) don't.

---
Repository: /testbed
