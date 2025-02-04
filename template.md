# 🧠 blue-assistant

🧠 `@assistant` runs AI scripts; DAGs that combine deterministic and AI operations.

--table--

```bash
pip install blue-assistant
```

```mermaid
graph LR
    assistant_script_list["@assistant script list"]
    assistant_script_run["@assistant script run~~- <script> <object-name>"]

    assistant_web_crawl["@assistant web crawl~~- <url-1>+<url-2>+<url-3> <object-name>"]

    script["📜 script"]:::folder
    url["🔗 url"]:::folder
    object["📂 object"]:::folder

    script --> assistant_script_list

    script --> assistant_script_run
    object --> assistant_script_run
    assistant_script_run --> object

    url --> assistant_web_crawl
    assistant_web_crawl --> object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

---

--signature--