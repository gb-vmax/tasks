# Bug Report

### Describe the bug

I'm experiencing an issue with remark where extensions are not being applied in the correct order. It seems like the configuration system has stopped working properly - when I pass multiple extensions, they either don't get applied at all or the behavior is completely broken.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
  .use(pluginA)
  .use(pluginB)
  .use(pluginC)

// Extensions from pluginB and pluginC don't seem to be applied correctly
const result = processor.processSync(markdown)
```

When I have multiple plugins/extensions configured, the later ones in the chain seem to override or interfere with earlier ones in unexpected ways. The output is completely different from what I'd expect based on the plugin order.

### Expected behavior

Extensions should be processed and applied in the order they are added. Each plugin should be able to build on top of the previous ones without breaking the configuration chain.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
