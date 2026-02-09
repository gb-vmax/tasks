# Bug Report

### Describe the bug

I'm encountering an issue with remark-directive where the `name` property is missing from directive nodes. When parsing text directives (and likely other directive types), the resulting AST nodes don't include the directive name, which breaks any code that relies on accessing `node.name`.

### Reproduction

```js
import { remarkDirective } from 'remark-directive';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const result = processor.parse(':myDirective[content]');

// Expected: node.name should be "myDirective"
// Actual: node.name is undefined
console.log(result.children[0].name); // undefined
```

### Expected behavior

Directive nodes should have a `name` property containing the directive's name (e.g., "myDirective" for `:myDirective[content]`). This is critical for identifying which directive is being used and processing it accordingly.

### Additional context

This seems to affect all directive types (text, leaf, and container directives). The directive name is essential for any practical use of the directive system, as you need to know which directive you're dealing with to apply the correct transformation or rendering logic.

---
Repository: /testbed
