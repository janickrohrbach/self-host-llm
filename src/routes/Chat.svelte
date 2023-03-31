<script lang="ts">
  import Message from "./ChatMessage.svelte";
  import Fa from "svelte-fa";
  import {faPaperPlane} from "@fortawesome/free-regular-svg-icons";

  let prompt: string | undefined;

  let messages = [{text: "Hi, how can I help you?", sentByMe: false}];

  async function getLLMResponse(message: string | undefined) {
    if (message != undefined) {
      prompt = undefined;
      messages.push({text: message, sentByMe: true});
      messages.push({text: "...", sentByMe: false});
      messages = messages; // this way svelte knows it updated

      const res = await fetch("http://127.0.0.1:8000/api", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({text: message}),
      });

      const json = await res.json();
      messages.pop();
      messages.push({text: json[0].generated_text, sentByMe: false});
      messages = messages;
    }
  }
</script>

<div class="chat">
  {#each messages as message}
    <div>
      <Message text={message.text} sentByMe={message.sentByMe} />
    </div>
  {/each}
  <form class="chat-input">
    <input
      type="text"
      placeholder="Ask the LLM ..."
      class="prompt"
      bind:value={prompt}
    />
    <button type="submit" class="send" on:click={() => getLLMResponse(prompt)}>
      <Fa icon={faPaperPlane} size="1x" />
    </button>
  </form>
</div>

<style>
  .chat {
    width: 75%;
  }

  .chat-input {
    margin-top: 50px;
    display: flex;
    justify-content: center;
  }

  .prompt {
    width: 60%;
    border-radius: 5px 0 0 5px;
    padding: 5px 10px;
    border: 0px;
  }

  .send {
    position: relative;
    border-radius: 0 5px 5px 0;
    border: 0px;
    width: 50px;
    background-color: #d2d6de;
  }
</style>
