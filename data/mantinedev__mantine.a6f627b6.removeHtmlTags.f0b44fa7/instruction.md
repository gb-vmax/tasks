# Bug Report

### Describe the bug

The `isNotEmptyHTML` validator is not correctly handling HTML strings with multiple tags. It seems like only the first HTML tag is being removed instead of all tags in the string.

### Reproduction

```js
import { isNotEmptyHTML } from '@mantine/form';

const validator = isNotEmptyHTML('Field cannot be empty');

// This should be invalid (empty after removing tags) but passes validation
const result1 = validator('<p></p><div></div>');

// This also behaves unexpectedly
const result2 = validator('<span>test</span><br/><p>more</p>');
```

### Expected behavior

The validator should strip all HTML tags from the input string, not just the first one. When multiple tags are present, they should all be removed before checking if the content is empty.

For example:
- `<p></p><div></div>` should be treated as empty
- `<span>test</span><p>more</p>` should extract "testmore" as the text content

### System Info
- @mantine/form version: latest
- Browser: Chrome 120

---
Repository: /testbed
