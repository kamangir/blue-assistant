# Hue 🔥

```yaml
script:
  vars:
    function_prompt: Complete this Python function to send a color command to a Hue light.
    function_signature: |
      def set_light_color(
          bridge_ip: str,
          username: str,
          light_id: str,
          hue: int,  # 0 to 65535
          saturation: int,  # 0 to 254
          verbose: bool = False,
      ) -> bool:
          logger.info(
              "{}.set_light_color({}@{}:{}) -> hue=0x{:x}, saturation=0x{:x}".format(
                  NAME,
                  username,
                  bridge_ip,
                  light_id,
                  hue,
                  saturation,
              )
          )

          ...

          return True
    bridge_ip_prompt: Generate instructions for finding my Hue bridge IP address.
    username_prompt: |
      Generate instructions for creating a developer username 
      on my Philips Hue Bridge
    light_id_prompt: |
      Generate instructions for finding the light ID of my Hue lights.

  nodes:
    generating_the_code:
      action: generate_text
      prompt: |
        :::function_prompt

        :::function_signature
      acquiring_bridge_ip:
        action: generate_text
        prompt: bridge_ip_prompt
      creating_username:
        action: generate_text
        prompt: username_prompt
        depends-on: acquiring_bridge_ip
      finding_light_id:
        action: generate_text
        prompt: light_id_prompt
        depends-on: creating_username

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
