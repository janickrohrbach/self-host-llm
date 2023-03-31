<script>
  import "./styles.css";
  import Fa from "svelte-fa";
  import {faGithub} from "@fortawesome/free-brands-svg-icons";
</script>

<div class="app">
  <main>
    <slot />
  </main>

  <footer>
    <a href="https://github.com/janickrohrbach/self-host-llm">
      <Fa icon={faGithub} size="3x" primaryColor="#3e3e3e" /></a
    >
  </footer>
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
    max-width: 64rem;
    margin: 0 auto;
    box-sizing: border-box;
  }

  footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 36px;
  }
</style>
