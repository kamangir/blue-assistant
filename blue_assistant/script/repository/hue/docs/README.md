# Hue 🔥

```yaml
script:
  vars:
    objective: Write a Python function to send a color command to a Hue light.
  nodes:
    generating_the_code:
      action: generate_text
      prompt: :::objective

```
[metadata.yaml](../metadata.yaml)

🔥

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue .
```


```yaml
{}

```

`TBA/metadata.yaml`

🔥

```bash
@hue set - \
  --bridge_ip TBA \
  --username TBA \
  --light_id TBA \
  --verbose 1
```

🔥

---

- [round 1](./round-1.md)
