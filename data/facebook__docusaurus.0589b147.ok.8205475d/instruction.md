# Bug Report

### Describe the bug

After a recent update, I'm getting an error `Maximum call limit exceeded` when processing MDX files. The error seems to be coming from somewhere deep in the remark-mdx parser, but I'm not doing anything unusual - just parsing standard MDX content.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here with **bold** text.

<Component prop="value" />

More content...
`

// This throws "Maximum call limit exceeded"
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any call limit errors. This was working fine before and I haven't changed my code - just updated dependencies.

### Additional context

The error message mentions something about a call count exceeding 100, but I'm only compiling a single MDX file. Not sure what's being called 100+ times internally or why there's suddenly a limit on it.

---
Repository: /testbed
