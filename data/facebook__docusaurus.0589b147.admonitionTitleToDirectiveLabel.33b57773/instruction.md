# Bug Report

### Describe the bug

I'm encountering an issue with admonition title processing in markdown content. When using the `admonitionTitleToDirectiveLabel` function, the regex replacement is not working correctly and the title is not being properly extracted from the admonition syntax.

### Reproduction

```js
import { admonitionTitleToDirectiveLabel } from '@docusaurus/utils';

const content = `
:::note My Title
Some content here
:::
`;

const result = admonitionTitleToDirectiveLabel(content, ['note', 'tip', 'warning']);
// The title "My Title" is not being processed correctly
console.log(result);
```

The function should convert admonition titles to directive labels, but it seems like the groups are not being captured properly from the regex match.

### Expected behavior

The function should correctly extract and process the title from admonition blocks like `:::note My Title` and apply the appropriate transformation.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
