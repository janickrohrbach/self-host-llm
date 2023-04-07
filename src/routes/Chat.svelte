<script lang="ts">
  import Message from "./ChatMessage.svelte";
  import Fa from "svelte-fa";
  import {faPaperPlane, faTrashCan} from "@fortawesome/free-regular-svg-icons";

  let prompt: string | undefined;

  let starting_message = {text: "Hi, how can I help you?", sentByMe: false};
  let messages = [starting_message];

  async function resetChat() {
    messages = [starting_message];
  }

  async function getLLMResponse(message: string | undefined) {
    if (message != undefined) {
      prompt = undefined;
      messages.push({text: message, sentByMe: true});
      messages.push({text: "...", sentByMe: false});
      messages = messages; // this way svelte knows it updated

      let custom_promt =
        (messages.length > 3 ? "Passage: " : "") +
        messages
          .slice(1, -2)
          .map((m) => m.text)
          .join(" ") +
        "\n\nQuestion: " +
        message;
      console.log(custom_promt);

      const res = await fetch("http://127.0.0.1:5000/api", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({text: custom_promt}),
      });

      const json = await res.json();
      messages.pop();
      messages.push({text: json[0].generated_text, sentByMe: false});
      messages = messages;
    }
  }
</script>

<div class="chat">
  <div class="chat-container">
    <div class="chat-messages">
      {#each messages as message}
        <div>
          <Message text={message.text} sentByMe={message.sentByMe} />
        </div>
      {/each}
    </div>
  </div>
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
    <button class="reset" on:click={() => resetChat()}
      ><Fa icon={faTrashCan} size="1x" /></button
    >
  </form>
</div>

<style>
  .chat {
    width: 75%;
  }

  .chat-container {
    height: 400px;
    overflow: auto;
    display: flex;
    flex-direction: column-reverse;
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

  .reset {
    position: relative;
    border-radius: 5px;
    border: 0px;
    width: 50px;
    background-color: #d2d6de;
    margin-left: 20px;
  }
</style>
