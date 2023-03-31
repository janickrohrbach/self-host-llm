<script lang="ts">
  import llamaLeft from "$lib/images/llama_left.png";
  import llamaRight from "$lib/images/llama_right.png";

  export let text: string;
  export let sentByMe: boolean;
</script>

<div class="message" class:right={sentByMe} class:left={!sentByMe}>
  {#if sentByMe}
    <div class="message__inner">
      <div class="message__bubble">{text}</div>
      <div class="message__spacer" />
    </div>
    <img src={llamaRight} alt="you" />
  {:else}
    <img src={llamaLeft} alt="llm" />
    <div class="message__inner">
      <div class="message__spacer" />
      <div class="message__bubble">{text}</div>
    </div>
  {/if}
</div>

<style>
  .message__bubble {
    position: relative;
    border-radius: 5px;
    padding: 5px 10px;
    background: #d2d6de;
    margin: 2px 0 5px 50px;
    margin-right: 15px;
    margin-left: 15px;
    max-width: 80%;
  }

  .left > .message__inner > .message__bubble:after {
    content: "";
    position: absolute;
    display: block;
    width: 0;
    z-index: 1;
    border-style: solid;
    border-color: transparent #d2d6de;
    border-width: 5px 5px 5px 0;
    top: 10px;
    left: -5px;
    margin-top: -5px;
  }

  .right > .message__inner > .message__bubble:after {
    content: "";
    position: absolute;
    display: block;
    width: 0;
    z-index: 1;
    border-style: solid;
    border-color: transparent #d2d6de;
    border-width: 5px 0px 5px 5px;
    top: 10px;
    right: -5px;
    margin-top: -5px;
  }

  .message {
    display: flex;
  }

  .message__inner {
    flex: 1;
    display: flex;
    flex-direction: row-reverse;
  }

  .message__spacer {
    flex: 1;
  }

  img {
    border-radius: 50%;
    float: left;
    width: 40px;
    height: 40px;
  }
  .right img {
    float: right;
  }
</style>
