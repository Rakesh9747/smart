---
title: Smart Institution
emoji: 🏫
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Smart Institution

This is a Django-based smart institution management system with AI integration.

## Deployment on Hugging Face Spaces

This project is configured to run on Hugging Face Spaces using Docker.

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the server:
   ```bash
   python manage.py runserver
   ```
