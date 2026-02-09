# Bug Report

### Describe the bug

The `isNotEmptyHTML` validator is not working correctly anymore. When I pass HTML content with tags, it's not being properly validated and the validator seems to fail at removing HTML tags from the input string.

### Reproduction

```js
import { isNotEmptyHTML } from '@mantine/form';

const validator = isNotEmptyHTML('Field cannot be empty');

// This should be considered empty after removing HTML tags
const result1 = validator('<p></p>');

// This should be valid
const result2 = validator('<p>Some content</p>');

// These cases are now behaving unexpectedly
const result3 = validator('<div><span></span></div>');
const result4 = validator('<br />');
```

### Expected behavior

The validator should strip all HTML tags from the input and then check if the remaining text is empty. Currently it seems like HTML tags are not being removed properly, causing validation to fail for inputs that should be considered empty.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
