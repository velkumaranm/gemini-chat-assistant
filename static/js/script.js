function sendPrompt() {
  const promptInput = document.getElementById("prompt");
  const prompt = promptInput.value.trim();
  if (!prompt) return;

  const chatBox = document.getElementById("chat-box");
  const timestamp = new Date().toLocaleTimeString();

  chatBox.innerHTML += `<div class="user-msg"><strong>You</strong><span class="timestamp">[${timestamp}]</span>: ${prompt}</div>`;
  document.getElementById("loading").style.display = "block";

  fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  })
    .then((res) => res.json())
    .then((data) => {
      const replyTime = new Date().toLocaleTimeString();
      chatBox.innerHTML += `<div class="gemini-msg"><strong>Gemini</strong><span class="timestamp">[${replyTime}]</span>: ${data.response}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
      document.getElementById("loading").style.display = "none";
    })
    .catch((err) => {
      chatBox.innerHTML += `<div class="gemini-msg"><strong>Gemini</strong>: ⚠️ Error: ${err.message}</div>`;
      document.getElementById("loading").style.display = "none";
    });

  promptInput.value = "";
}
