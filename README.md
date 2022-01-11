# Falcon app quick start

This is a template for creating a Falcon-based API, all neatly wrapped in docker and routed through nginx.
It does SSL (https) too, just fill the blanks in *docker-compose.yml*.

```
.
├── Dockerfile (app dockerfile)
├── app (root dir of the Falcon app)
│   ├── __init__.py
│   ├── conf.py
│   ├── log.py
│   └── main.py
├── default.conf (example nginx conf)
├── docker-compose.yml (set https here)
└── requirements.txt (app dependencies)
```