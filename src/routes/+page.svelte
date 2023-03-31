<script>
  import Chat from "./Chat.svelte";
</script>

<svelte:head>
  <title>Self-host LLM</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
  <h1 class="welcome">Start chatting 🥳</h1>

  <Chat />
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 0.6;
  }

  h1 {
    width: 100%;
  }

  .welcome {
    display: block;
    position: relative;
    width: 100%;
    height: 0;
    padding: 0 0 50px 0;
  }
</style>
