# Hue - round 1

```yaml
include:::noref ../metadata-round-1.yaml
```
[metadata.yaml](../metadata-round-1.yaml)

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue . \
  --verbose 1
```

set:::object_name hue-2025-03-13-urcan3

metadata:::get:::object_name

`get:::object_name/metadata.yaml`