# 🧠 blue-assistant

🧠 `@assistant` runs AI scripts, such as the ones listed below.

```bash
pip install blue-assistant
```

```mermaid
graph LR
    assistant_script_list["@assistant script list"]
    assistant_script_run["@assistant script run~~- <script> <object-name>"]

    script["📜 script"]:::folder
    object["📂 object"]:::folder

    script --> assistant_script_list

    script --> assistant_script_run
    object --> assistant_script_run
    assistant_script_run --> object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

--table--

---

--signature--