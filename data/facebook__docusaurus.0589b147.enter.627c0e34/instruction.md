# Bug Report

### Describe the bug

I'm experiencing an issue with token tracking in the markdown parser. When creating tokens with custom fields, the events array doesn't receive the actual token object that gets pushed to the stack. This causes a mismatch between what's tracked in the stack and what's recorded in the events.

### Reproduction

```js
// When entering a token with custom fields
const customFields = { custom: 'data' };
enter('paragraph', customFields);

// The stack contains the token with type and start time
// But the events array contains a different object (empty {})
// This breaks any code that relies on event/stack consistency
```

### Expected behavior

The same token object should be used in both the stack and the events array. When I pass custom fields to `enter()`, those fields should be preserved in the events that get recorded, not replaced with an empty object.

### Additional context

This seems to affect token lifecycle tracking where the enter and exit events need to reference the same token object. The inconsistency between what's pushed to the stack versus what's added to events causes problems when trying to match up enter/exit pairs or access token properties from the events array.

---
Repository: /testbed
