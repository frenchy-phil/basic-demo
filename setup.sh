#!/bin/bash
gunicorn --bind 0.0.0.0:$PORT serveur1 --daemon && sleep 2