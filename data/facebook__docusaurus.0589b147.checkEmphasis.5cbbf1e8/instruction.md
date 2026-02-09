# Bug Report

### Describe the bug

I'm encountering an issue with emphasis markers in markdown serialization. When I try to use emphasis in my markdown content, I'm getting an error message saying that the emphasis marker is invalid, even though I'm using valid markers (`*` or `_`).

### Reproduction

```js
import {toMarkdown} from 'mdast-util-to-markdown'

const tree = {
  type: 'emphasis',
  children: [{type: 'text', value: 'hello'}]
}

// This throws an error unexpectedly
const result = toMarkdown(tree, {emphasis: '*'})
```

The error message says:
```
Cannot serialize emphasis with `*` for `options.emphasis`, expected `*`, or `_`
```

This doesn't make sense - I'm using `*` which should be valid according to the error message itself.

### Expected behavior

The code should successfully serialize emphasis using either `*` or `_` as markers without throwing an error. Both are standard markdown emphasis markers and should be accepted.

### Additional context

This seems to affect any usage of emphasis in markdown serialization. Even the default behavior (without specifying an emphasis option) is now throwing errors when it shouldn't.

---
Repository: /testbed
