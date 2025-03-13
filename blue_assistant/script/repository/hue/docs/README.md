# Hue 🔥

```yaml
script:
  vars:
    objective: Write Python + Bash code to send a color command to the Hue LED lights in my apartment.
  nodes:
    generating_the_code:
      action: generate_text
      prompt: >
        :::objective

```
[metadata.yaml](../metadata.yaml)

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue . \
  --verbose 1
```



<details>
<summary>output</summary>

```yaml
output:
  script:
    nodes:
      generating_the_code:
        action: generate_text
        completed: true
        output: "To control Philips Hue lights using Python, you'll typically interact\
          \ with the Hue API. Below is a combination of Python and bash scripts that\
          \ allow you to send a color command to your Hue lights. First, ensure you\
          \ have the necessary libraries and setup:\n\n1. **Python Script: `set_hue_color.py`**\n\
          \n```python\nimport requests\nimport json\n\n# Replace with the IP address\
          \ of your Hue bridge and the username obtained during setup\nBRIDGE_IP =\
          \ '192.168.1.2'\nUSERNAME = 'your_username'\n\n# Function to change light\
          \ color\ndef set_light_color(light_id, hue, sat, bri):\n    url = f\"http://{BRIDGE_IP}/api/{USERNAME}/lights/{light_id}/state\"\
          \n    \n    # Hue API expects hue values from 0-65535\n    # Saturation\
          \ and brightness values should be between 0-254\n    payload = json.dumps({\n\
          \        \"on\": True,\n        \"hue\": hue,\n        \"sat\": sat,\n \
          \       \"bri\": bri\n    })\n    \n    response = requests.put(url, data=payload)\n\
          \    \n    if response.status_code == 200:\n        print(f\"Successfully\
          \ changed the light {light_id} color.\")\n    else:\n        print(f\"Failed\
          \ to change the light {light_id} color. Response: {response.text}\")\n\n\
          # Example usage\nset_light_color(light_id=1, hue=10000, sat=200, bri=254)\n\
          ```\n\n2. **Bash Script: `run_hue_script.sh`**\n\n```bash\n#!/bin/bash\n\
          \n# Activate your virtual environment if needed\n# source /path/to/your/venv/bin/activate\n\
          \n# Run the Python script\npython3 set_hue_color.py\n```\n\n3. **How to\
          \ Use:**\n\n   - **Find Your Bridge IP and Username:**\n     You can find\
          \ your bridge IP address through the Hue app. You'll also need to create\
          \ a username by interacting with the Hue API. Run the following bash command\
          \ to create a new user:\n\n     ```bash\n     curl -X POST -d '{\"devicetype\"\
          :\"my_hue_app#myscript\"}' http://<BRIDGE_IP>/api\n     ```\n\n     Follow\
          \ the instructions (usually pressing the bridge button) to obtain the username.\n\
          \n   - **Set Desired Color:**\n     Adjust the `hue`, `sat`, and `bri` parameters\
          \ in the Python script to set the desired color. Hue is a cyclic value (0-65535)\
          \ that covers the color spectrum, saturation adjusts the intensity of the\
          \ color, and brightness controls how bright the light will be.\n\n   - **Run\
          \ the Bash Script:**\n     Make your bash script executable and run it.\n\
          \n     ```bash\n     chmod +x run_hue_script.sh\n     ./run_hue_script.sh\n\
          \     ```\n\n**Note:** You may need to install the `requests` library if\
          \ it's not already available:\n\n```bash\npip install requests\n```\n\n\
          Replace `BRIDGE_IP` and `USERNAME` with your corresponding Philips Hue Bridge\
          \ details to make it functional. Make sure your Philips Hue bridge and device\
          \ running the script are on the same network."
        prompt: ':::objective

          '
    vars:
      objective: Write Python + Bash code to send a color command to the Hue LED lights
        in my apartment.
script:
  nodes:
    generating_the_code:
      action: generate_text
      prompt: ':::objective

        '
  vars:
    objective: Write Python + Bash code to send a color command to the Hue LED lights
      in my apartment.

```

</details>


🔥
