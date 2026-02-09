# Bug Report

### Describe the bug

I'm experiencing an issue with MDX text expressions not being serialized correctly to markdown. When trying to convert MDX content that contains inline/text expressions (like `{variable}` within a paragraph), the serialization process fails.

### Reproduction

```js
import {toMarkdown} from 'mdast-util-to-markdown'
import {mdxExpressionToMarkdown} from '@mdx-js/mdx'

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        {type: 'text', value: 'Hello '},
        {type: 'mdxTextExpression', value: 'name'},
        {type: 'text', value: '!'}
      ]
    }
  ]
}

// This throws an error or produces incorrect output
const markdown = toMarkdown(tree, {
  extensions: [mdxExpressionToMarkdown()]
})
```

### Expected behavior

The markdown serializer should properly handle `mdxTextExpression` nodes and convert them back to their `{expression}` syntax. The output should be something like:
```
Hello {name}!
```

### Additional context

This seems to have broken recently. Flow expressions (block-level `{expression}`) still work fine, but inline text expressions within paragraphs are not being handled properly.

---
Repository: /testbed
