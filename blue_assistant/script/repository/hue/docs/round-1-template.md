# Hue - round 1

```yaml
--include--noref ../metadata.yaml
```
[metadata.yaml](../metadata.yaml)

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue . \
  --verbose 1
```

set:::object_name hue-2025-03-13-urcan3

yaml:::get:::object_name