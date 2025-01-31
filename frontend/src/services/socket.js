const socket = new WebSocket('ws://localhost:8000/ws/chat/');

export const sendMessage = (message) => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({ message }));
  }
};

export const onMessage = (callback) => {
  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    callback(data);
  };
};