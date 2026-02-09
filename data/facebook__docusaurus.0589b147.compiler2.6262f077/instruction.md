# Bug Report

### Describe the bug

I'm experiencing an issue where custom markdown settings are being overridden when using the remark stringify compiler. It seems like the order of how options are merged has changed, causing user-provided settings to be ignored in favor of plugin defaults.

### Reproduction

```js
const remark = require('remark');

const processor = remark()
  .data('settings', { bullet: '-' })
  .use(remarkStringify, { bullet: '*' });

const result = processor.stringify({
  type: 'root',
  children: [
    {
      type: 'list',
      ordered: false,
      children: [
        {
          type: 'listItem',
          children: [{ type: 'text', value: 'item' }]
        }
      ]
    }
  ]
});

// Expected: Uses '*' as bullet (from options)
// Actual: Uses '-' as bullet (from data settings)
```

### Expected behavior

When passing options directly to `remarkStringify`, those options should take precedence over the settings stored in `data('settings')`. The user-provided configuration should have the highest priority.

### Additional context

This appears to have broken after a recent update. Previously, options passed to the plugin would correctly override any default settings, but now they seem to be getting overwritten instead.

---
Repository: /testbed
