# Hue 🔥

```yaml
script:
  vars:
    objective: Write Python + Bash code to send a color command to the Hue LED lights in my apartment.
  nodes:
    generating_the_code:
      action: generate_text
      prompt: :::objective

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
        output: "To send commands to your Philips Hue lights, you'll need to interact\
          \ with the Philips Hue Bridge using its API. This process involves a few\
          \ key steps, such as discovering your Hue Bridge, creating a user/API key,\
          \ and then sending commands. Below is an example combining Python and Bash\
          \ to change light colors. You'll need to have the `requests` module available\
          \ in Python and make sure you have access to your local network where the\
          \ Hue Bridge is located.\n\n### Prerequisites\n\n1. **Find Your Hue Bridge\
          \ IP**: You can use `nmap` or any other network scanner to find the IP of\
          \ the Hue Bridge. Typically, it's also discoverable via the Philips Hue\
          \ app.\n  \n2. **Create a Hue API User**: You'll need to press the link\
          \ button on your Hue Bridge and execute an API call to create an API user.\n\
          \n### Python Code (main.py)\n\nThis script sends a color change command\
          \ to the Philips Hue lights using the Hue Bridge API. It requires the `requests`\
          \ library, which you can install via pip if not available (`pip install\
          \ requests`).\n\n```python\nimport requests\nimport json\n\nHUE_BRIDGE_IP\
          \ = \"192.168.1.2\"  # Replace with your Hue Bridge IP address\nAPI_USERNAME\
          \ = \"your_api_username\"  # Replace with the API username you created\n\
          LIGHT_ID = \"1\"  # Replace with the ID of the light you want to control\n\
          \ndef set_light_color(light_id, hue, sat, bri):\n    url = f\"http://{HUE_BRIDGE_IP}/api/{API_USERNAME}/lights/{light_id}/state\"\
          \n    payload = {\n        \"on\": True,\n        \"hue\": hue,\n      \
          \  \"sat\": sat,\n        \"bri\": bri\n    }\n    \n    response = requests.put(url,\
          \ data=json.dumps(payload))\n    if response.status_code == 200:\n     \
          \   print(\"Command sent successfully\")\n    else:\n        print(f\"Failed\
          \ to send command: {response.status_code} - {response.text}\")\n\n# Example\
          \ usage: Setting the light to a bright red color\nset_light_color(LIGHT_ID,\
          \ hue=0, sat=254, bri=254)\n```\n\n### Bash Script (run.sh)\n\nThis script\
          \ simply runs the Python code and can be used to automate or integrate this\
          \ process in a larger bash script.\n\n```bash\n#!/bin/bash\n\n# Run the\
          \ Python script to set the color of the Hue lights\npython3 main.py\n```\n\
          \n### Instructions\n\n1. **Install Required Python Packages**: Make sure\
          \ you have the `requests` package installed in your Python environment.\n\
          \   \n   ```bash\n   pip install requests\n   ```\n\n2. **Update the Python\
          \ Script**:\n   - Replace `HUE_BRIDGE_IP` with the IP address of your Hue\
          \ Bridge.\n   - Replace `API_USERNAME` with the username you get by creating\
          \ a Hue API user.\n   - Replace `LIGHT_ID` with the ID of the light you\
          \ intend to control (you can use the API to list the lights and find IDs).\n\
          \n3. **Creating an API User**:\n   - Press the button on your Hue Bridge.\n\
          \   - Use a tool like `curl` to register a new API user (while the button\
          \ is pressed):\n\n     ```bash\n     curl -X POST -d '{ \"devicetype\":\
          \ \"my_app#test\" }' http://<bridge_ip_address>/api\n     ```\n\n   - Note\
          \ the username from the response and use it in your scripts.\n\n4. **Execute\
          \ the Bash Script**:\n\n   Run the Bash script to change the color of the\
          \ light:\n\n   ```bash\n   chmod +x run.sh\n   ./run.sh\n   ```\n\nThis\
          \ will send a request to the Hue Bridge to change the specified light to\
          \ the desired color. You can modify the `hue`, `sat`, and `bri` values in\
          \ `set_light_color` to achieve different colors and brightness levels."
        prompt: :::objective
    vars:
      objective: Write Python + Bash code to send a color command to the Hue LED lights
        in my apartment.
script:
  nodes:
    generating_the_code:
      action: generate_text
      prompt: :::objective
  vars:
    objective: Write Python + Bash code to send a color command to the Hue LED lights
      in my apartment.

```

</details>


🔥
