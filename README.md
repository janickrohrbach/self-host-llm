## Self-host LLM

ChatGPT like functionality to be self-hosted. This uses
[Flan-Alpaca](https://github.com/declare-lab/flan-alpaca) large model. Model can be
changed to any other Flan-Alpaca model in
[src/self_host_llm/config.yaml](src/self_host_llm/config.yaml).

![Conversation Screenshot](public/conversation_screenshot.png)

# Backend

Uses Python FastAPI to serve the model.

## Developing

Install the Python in editable mode with dev dependencies and start the uvicorn server
to start working.

```bash
pip install -e ".[dev]"
uvicorn self_host_llm.main:app --reload
```

## Building

Build the wheel file.

```bash
pip install build
build --wheel
```

# Frontend

Simple chat UI built with SvelteKit.

## Developing

Once you've created a project and installed dependencies with `npm install`, start a
development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an
> [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.
