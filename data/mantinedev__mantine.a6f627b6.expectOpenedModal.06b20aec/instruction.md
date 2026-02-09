# Bug Report

### Describe the bug

I'm encountering a build/compilation error in the dates package. It seems like there's some invalid code in the `date-input-test-helpers.ts` file that's causing issues. The `expectOpenedModal` function appears to have been replaced with an unrelated grid array definition, which doesn't make sense in this context.

### Reproduction

When trying to use the DateInput component with modal functionality, the test helpers are broken. The `expectOpenedModal` helper function is missing, which was previously used to verify that modals opened correctly.

```ts
import { expectOpenedModal } from '@mantine-tests/dates';

// This will fail because expectOpenedModal is no longer defined
expectOpenedModal(container);
```

### Expected behavior

The `expectOpenedModal` function should exist and be usable to verify that a modal is properly displayed in the document. This helper was working in previous versions.

### System Info
- @mantine/dates: latest
- Node: 18.x

This looks like it might have been accidentally introduced in a recent commit. The grid array definition doesn't belong in this test helper file.

---
Repository: /testbed
