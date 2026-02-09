# Bug Report

### Describe the bug

The `getEditUrl` function is generating incorrect URLs for edit links. When I try to use the edit functionality, the generated URLs contain backslashes instead of forward slashes, which breaks the links on GitHub/GitLab.

### Reproduction

```js
import { getEditUrl } from '@docusaurus/utils';

const editUrl = 'https://github.com/user/repo/edit/main';
const filePath = 'docs/intro.md';

const result = getEditUrl(filePath, editUrl);
console.log(result);
// Expected: https://github.com/user/repo/edit/main/docs/intro.md
// Actual: https://github.com/user/repo/edit/main/docs\intro.md
```

Also noticed that when `editUrl` is not provided, it returns an empty string instead of `undefined`, which might cause issues with conditional rendering.

### Expected behavior

- Edit URLs should always use forward slashes (`/`) regardless of the platform
- When `editUrl` is not provided, the function should return `undefined` (not an empty string)

### System Info
- Docusaurus version: latest
- OS: Windows 11

---
Repository: /testbed
