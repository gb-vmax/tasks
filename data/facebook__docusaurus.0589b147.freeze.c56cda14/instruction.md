# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where plugins aren't being applied correctly. It seems like some plugins are being skipped during the freeze process, leading to unexpected behavior in the output.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

const processor = compile('# Hello', {
  remarkPlugins: [
    pluginA,
    pluginB,
    pluginC
  ]
})
```

When I have multiple plugins configured, it appears that the first plugin in the array is being skipped entirely. The transformations from `pluginA` don't get applied to my MDX content, but `pluginB` and `pluginC` work as expected.

### Expected behavior

All configured plugins should be applied in order, including the first one in the array. The processor should freeze correctly and execute all registered transformers.

### Additional context

This seems to have started happening recently. I noticed that when I move my plugins around in the array, whichever plugin is in the first position gets skipped. Moving a plugin to the second position makes it work again.

---
Repository: /testbed
